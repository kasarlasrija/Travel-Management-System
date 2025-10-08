# main.py
"""
Command-line entry point for the Travel Management System.
Use this to test services for users, destinations, packages,
bookings, payments, travels, and reviews.
"""

from src.config import get_supabase
from src.services.user_service import user_service
from src.services.destination_service import destination_service
from src.services.package_service import package_service
from src.services.booking_service import booking_service
from src.services.payment_service import payment_service
from src.services.travel_service import travel_service
from src.services.review_service import review_service


def test_supabase_connection():
    print("\n🔍 Testing Supabase connection...")
    try:
        sb = get_supabase()
        data = sb.table("users").select("*").limit(1).execute()
        print("✅ Supabase connection successful!")
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")


def manage_users():
    print("\n👤 USER MANAGEMENT")
    print("1. List users\n2. Add user")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        users = user_service.list_users()
        for u in users:
            print(u)
    elif ch == "2":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        password = input("Password: ")
        role = input("Role (Traveler/Admin): ")
        user = user_service.add_user(name, email, phone, password, role)
        print("✅ User added:", user)


def manage_destinations():
    print("\n📍 DESTINATION MANAGEMENT")
    print("1. List destinations\n2. Add destination")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        dests = destination_service.list_destinations()
        for d in dests:
            print(d)
    elif ch == "2":
        name = input("Name: ")
        country = input("Country: ")
        dtype = input("Type (Adventure/Leisure/Cultural): ")
        desc = input("Description: ")
        dest = destination_service.add_destination(name, country, dtype, desc)
        print("✅ Destination added:", dest)


def manage_packages():
    print("\n🎒 PACKAGE MANAGEMENT")
    print("1. List packages\n2. Add package")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        pkgs = package_service.list_packages()
        for p in pkgs:
            print(p)
    elif ch == "2":
        dest_id = int(input("Destination ID: "))
        name = input("Name: ")
        price = float(input("Price: "))
        days = int(input("Days: "))
        details = input("Details: ")
        pkg = package_service.add_package(dest_id, name, price, days, details)
        print("✅ Package added:", pkg)


def manage_bookings():
    print("\n📘 BOOKING MANAGEMENT")
    print("1. List bookings\n2. Create booking")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        bookings = booking_service.list_bookings()
        for b in bookings:
            print(b)
    elif ch == "2":
        user_id = int(input("User ID: "))
        package_id = int(input("Package ID: "))
        status = input("Status (PLACED/PENDING/CANCELLED/COMPLETED): ")
        total = float(input("Total amount: "))
        booking = booking_service.create_booking(user_id, package_id, status, total)
        print("✅ Booking created:", booking)


def manage_payments():
    print("\n💳 PAYMENT MANAGEMENT")
    print("1. List payments\n2. Make payment")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        payments = payment_service.list_payments()
        for p in payments:
            print(p)
    elif ch == "2":
        booking_id = int(input("Booking ID: "))
        amount = float(input("Amount: "))
        status = input("Status (SUCCESS/FAILED/REFUNDED): ")
        payment = payment_service.make_payment(booking_id, amount, status)
        print("✅ Payment recorded:", payment)


def manage_travels():
    print("\n🗺️ TRAVEL ITINERARY MANAGEMENT")
    print("1. List travels\n2. Add travel itinerary")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        travels = travel_service.list_travels()
        for t in travels:
            print(t)
    elif ch == "2":
        user_id = int(input("User ID: "))
        package_id = int(input("Package ID: "))
        day_plan = input("Day Plan: ")
        assist = input("Assistance Notes: ")
        travel = travel_service.create_travel(user_id, package_id, day_plan, assist)
        print("✅ Travel record added:", travel)


def manage_reviews():
    print("\n⭐ REVIEW MANAGEMENT")
    print("1. List reviews\n2. Add review")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        reviews = review_service.list_reviews()
        for r in reviews:
            print(r)
    elif ch == "2":
        user_id = int(input("User ID: "))
        package_id = int(input("Package ID: "))
        rating = int(input("Rating (1-5): "))
        comment = input("Comment: ")
        review = review_service.add_review(user_id, package_id, rating, comment)
        print("✅ Review added:", review)


def main():
    print("\n===============================")
    print("🚀 TRAVEL MANAGEMENT SYSTEM CLI")
    print("===============================\n")
    print("1. Test Supabase Connection")
    print("2. Manage Users")
    print("3. Manage Destinations")
    print("4. Manage Packages")
    print("5. Manage Bookings")
    print("6. Manage Payments")
    print("7. Manage Travels")
    print("8. Manage Reviews")
    print("0. Exit")

    while True:
        ch = input("\nEnter choice: ").strip()
        if ch == "1":
            test_supabase_connection()
        elif ch == "2":
            manage_users()
        elif ch == "3":
            manage_destinations()
        elif ch == "4":
            manage_packages()
        elif ch == "5":
            manage_bookings()
        elif ch == "6":
            manage_payments()
        elif ch == "7":
            manage_travels()
        elif ch == "8":
            manage_reviews()
        elif ch == "0":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
