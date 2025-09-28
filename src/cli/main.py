import argparse
from src.services.destination_service import destination_service
from src.services.package_service import package_service
from src.services.booking_service import booking_service
from src.services.payment_service import payment_service
from src.services.travel_service import travel_service
from src.services.review_service import review_service

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Travel Management System CLI")
        subparsers = self.parser.add_subparsers(dest="command")

        # --- DESTINATION COMMANDS ---
        destination_parser = subparsers.add_parser("destination", help="Manage destinations")
        dest_subparsers = destination_parser.add_subparsers(dest="action")

        dest_add_parser = dest_subparsers.add_parser("add", help="Add a destination")
        dest_add_parser.add_argument("--name", type=str, required=True)
        dest_add_parser.add_argument("--description", type=str, required=True)
        dest_add_parser.set_defaults(func=self._cmd_destination_add)

        dest_list_parser = dest_subparsers.add_parser("list", help="List all destinations")
        dest_list_parser.set_defaults(func=self._cmd_destination_list)

        # --- PACKAGE COMMANDS ---
        package_parser = subparsers.add_parser("package", help="Manage packages")
        pkg_subparsers = package_parser.add_subparsers(dest="action")

        pkg_add_parser = pkg_subparsers.add_parser("add", help="Add a package")
        pkg_add_parser.add_argument("--destination_id", type=int, required=True)
        pkg_add_parser.add_argument("--name", type=str, required=True)
        pkg_add_parser.add_argument("--price", type=float, required=True)
        pkg_add_parser.set_defaults(func=self._cmd_package_add)

        pkg_list_parser = pkg_subparsers.add_parser("list", help="List all packages")
        pkg_list_parser.set_defaults(func=self._cmd_package_list)

        # --- BOOKING COMMANDS ---
        booking_parser = subparsers.add_parser("booking", help="Manage bookings")
        booking_subparsers = booking_parser.add_subparsers(dest="action")

        booking_add_parser = booking_subparsers.add_parser("add", help="Add a booking")
        booking_add_parser.add_argument("--user_id", type=int, required=True)
        booking_add_parser.add_argument("--package_id", type=int, required=True)
        booking_add_parser.add_argument("--status", type=str, required=True)
        booking_add_parser.set_defaults(func=self._cmd_booking_add)

        booking_list_parser = booking_subparsers.add_parser("list", help="List all bookings")
        booking_list_parser.set_defaults(func=self._cmd_booking_list)

        # --- PAYMENT COMMANDS ---
        payment_parser = subparsers.add_parser("payment", help="Manage payments")
        payment_subparsers = payment_parser.add_subparsers(dest="action")

        payment_add_parser = payment_subparsers.add_parser("add", help="Add a payment")
        payment_add_parser.add_argument("--booking_id", type=int, required=True)
        payment_add_parser.add_argument("--amount", type=float, required=True)
        payment_add_parser.add_argument("--status", type=str, required=True)
        payment_add_parser.set_defaults(func=self._cmd_payment_add)

        payment_list_parser = payment_subparsers.add_parser("list", help="List all payments")
        payment_list_parser.set_defaults(func=self._cmd_payment_list)

        # --- TRAVEL (Itinerary & Assistance) COMMANDS ---
        travel_parser = subparsers.add_parser("travel", help="Manage travel itineraries and assistance")
        travel_subparsers = travel_parser.add_subparsers(dest="action")

        travel_add_parser = travel_subparsers.add_parser("add", help="Add a travel itinerary/assistance")
        travel_add_parser.add_argument("--user_id", type=int, required=True)
        travel_add_parser.add_argument("--package_id", type=int, required=True)
        travel_add_parser.add_argument("--day_plan", type=str, required=True)
        travel_add_parser.add_argument("--assistance_notes", type=str, required=True)
        travel_add_parser.set_defaults(func=self._cmd_travel_add)

        travel_list_parser = travel_subparsers.add_parser("list", help="List all travel records")
        travel_list_parser.set_defaults(func=self._cmd_travel_list)

        # --- REVIEW & FEEDBACK COMMANDS ---
        review_parser = subparsers.add_parser("review", help="Manage reviews")
        review_subparsers = review_parser.add_subparsers(dest="action")

        review_add_parser = review_subparsers.add_parser("add", help="Add a review")
        review_add_parser.add_argument("--user_id", type=int, required=True)
        review_add_parser.add_argument("--package_id", type=int, required=True)
        review_add_parser.add_argument("--rating", type=int, required=True, help="Rating (1-5)")
        review_add_parser.add_argument("--comment", type=str, required=True)
        review_add_parser.set_defaults(func=self._cmd_review_add)

        review_list_parser = review_subparsers.add_parser("list", help="List all reviews")
        review_list_parser.set_defaults(func=self._cmd_review_list)

    # ---------------- COMMAND HANDLERS ----------------
    def _cmd_destination_add(self, args):
        dest = destination_service.add_destination(args.name, args.description)
        print("Destination added:", dest)

    def _cmd_destination_list(self, args):
        dests = destination_service.list_destinations()
        print("Destinations:", dests)

    def _cmd_package_add(self, args):
        pkg = package_service.add_package(args.destination_id, args.name, args.price)
        print("Package added:", pkg)

    def _cmd_package_list(self, args):
        pkgs = package_service.list_packages()
        print("Packages:", pkgs)

    def _cmd_booking_add(self, args):
        booking = booking_service.create_booking(args.user_id, args.package_id, args.status)
        print("Booking added:", booking)

    def _cmd_booking_list(self, args):
        bookings = booking_service.list_bookings()
        print("Bookings:", bookings)

    def _cmd_payment_add(self, args):
        payment = payment_service.make_payment(args.booking_id, args.amount, args.status)
        print("Payment added:", payment)

    def _cmd_payment_list(self, args):
        payments = payment_service.list_payments()
        print("Payments:", payments)

    def _cmd_travel_add(self, args):
        travel = travel_service.create_travel(args.user_id, args.package_id, args.day_plan, args.assistance_notes)
        print("Travel record added:", travel)

    def _cmd_travel_list(self, args):
        travels = travel_service.list_travels()
        print("Travel records:", travels)

    def _cmd_review_add(self, args):
        review = review_service.add_review(args.user_id, args.package_id, args.rating, args.comment)
        print("Review added:", review)

    def _cmd_review_list(self, args):
        reviews = review_service.list_reviews()
        print("Reviews:", reviews)

    # ---------------- RUN ----------------
    def run(self):
        args = self.parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:
            self.parser.print_help()


if __name__ == "__main__":
    cli = CLI()
    cli.run()
