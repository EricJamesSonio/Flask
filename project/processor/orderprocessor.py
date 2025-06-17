from ..model.order import Order
from ..model.receipt import Receipt
from extension import db


class OrderCalculator:
    @staticmethod
    def get_total(order: Order):
        return sum(item.quantity * item.price for item in order.orders)

    @staticmethod
    def get_discount(total, discount_rate):
        return total * (discount_rate / 100)

    @staticmethod
    def get_subtotal(total, discounted_price):
        return total - discounted_price

    @staticmethod
    def calculate(order, discount_rate=0.0):
        total = OrderCalculator.get_total(order)
        discounted_price = OrderCalculator.get_discount(total, discount_rate)
        subtotal = OrderCalculator.get_subtotal(total, discounted_price)

        return {
            "total": total,
            "discounted_price": discounted_price,
            "subtotal": subtotal,
        }


class OrderProcessor:
    @staticmethod
    def generate_order_code():
        last_order = Order.query.order_by(Order.id.desc()).first()
        next_id = 1 if not last_order else last_order.id + 1
        return f"ORD-{str(next_id).zfill(6)}"

    @staticmethod
    def generate_receipt_code():
        last_receipt = Receipt.query.order_by(Receipt.id.desc()).first()
        next_id = 1 if not last_receipt else last_receipt.id + 1
        return f"RCP-{str(next_id).zfill(6)}"

    @staticmethod
    def process_order(order: Order, amount_paid: float, discount_rate: float = 0.0):
        # Step 1: Generate and assign Order Code
        order.order_code = OrderProcessor.generate_order_code()

        # Step 2: Calculate prices
        calculation = OrderCalculator.calculate(order, discount_rate)
        total = calculation["total"]
        discounted_price = calculation["discounted_price"]
        subtotal = calculation["subtotal"]

        # Step 3: Validate payment
        if amount_paid < subtotal:
            raise ValueError("Insufficient Payment! Amount is less than the subtotal.")

        # Step 4: Save order
        db.session.add(order)
        db.session.flush()  # ensures order.id is generated before receipt creation

        # Step 5: Create and save receipt
        receipt = Receipt(
            order_id=order.id,
            receipt_code=OrderProcessor.generate_receipt_code(),
            total_amount=total,
            discount=discounted_price,
            subtotal=subtotal,
            amount_paid=amount_paid,
            change=amount_paid - subtotal,
        )
        db.session.add(receipt)
        db.session.commit()

        return receipt
