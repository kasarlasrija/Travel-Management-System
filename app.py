# app.py
import streamlit as st
from src.config import get_supabase

# Import services (make sure these modules exist and export the singleton objects)
from src.services.user_service import user_service
from src.services.destination_service import destination_service
from src.services.package_service import package_service
from src.services.booking_service import booking_service
from src.services.payment_service import payment_service
from src.services.travel_service import travel_service
from src.services.review_service import review_service

st.set_page_config(page_title="Travel Management System", layout="wide")
st.title("Travel Management System")

# initialize — ensures config loaded early, errors shown if keys missing
try:
    _ = get_supabase()
except Exception as e:
    st.error(f"Supabase config error: {e}")
    st.stop()

# ------------------- DESTINATIONS -------------------
st.header("Available Destinations")
col_d1, col_d2 = st.columns([2, 1])

with col_d1:
    try:
        dests = destination_service.list_destinations()
        if not dests:
            st.info("No destinations found.")
        else:
            for d in dests:
                # show core fields — adapt keys to your DB (dest_id, name, country, type, description)
                st.markdown(f"**{d.get('dest_id')} — {d.get('name')}**  \n"
                            f"{d.get('country', '')} • {d.get('type', '')}  \n"
                            f"{d.get('description', '')}")
    except Exception as e:
        st.error(f"Error fetching destinations: {e}")

with col_d2:
    st.subheader("Add Destination")
    with st.form("add_dest"):
        d_name = st.text_input("Name")
        d_country = st.text_input("Country")
        d_type = st.text_input("Type (Adventure/Leisure/Cultural)")
        d_description = st.text_area("Description")
        if st.form_submit_button("Add Destination"):
            try:
                dest = destination_service.add_destination(d_name, d_country, d_type, d_description)
                st.success(f"Destination added (id={dest.get('dest_id') if dest else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to add destination: {e}")

st.markdown("---")

# ------------------- PACKAGES -------------------
st.header("Packages")
col_p1, col_p2 = st.columns([2, 1])

with col_p1:
    try:
        packages = package_service.list_packages()
        if not packages:
            st.info("No packages found.")
        else:
            for p in packages:
                st.markdown(f"**{p.get('package_id')} — {p.get('name')}**  \n"
                            f"Destination ID: {p.get('dest_id')} • Days: {p.get('days')}  \n"
                            f"Price: {p.get('price')}  \n"
                            f"{p.get('details','')}")
    except Exception as e:
        st.error(f"Error fetching packages: {e}")

with col_p2:
    st.subheader("Add Package")
    with st.form("add_pkg"):
        pkg_dest_id = st.number_input("Destination ID", min_value=1, step=1)
        pkg_name = st.text_input("Package Name")
        pkg_price = st.number_input("Price", min_value=0.0, format="%.2f")
        pkg_days = st.number_input("Days", min_value=1, step=1)
        pkg_details = st.text_area("Details")
        if st.form_submit_button("Add Package"):
            try:
                pkg = package_service.add_package(int(pkg_dest_id), pkg_name, float(pkg_price), int(pkg_days), pkg_details)
                st.success(f"Package added (id={pkg.get('package_id') if pkg else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to add package: {e}")

st.markdown("---")

# ------------------- USERS -------------------
st.header("Users")
col_u1, col_u2 = st.columns([2, 1])

with col_u1:
    try:
        users = user_service.list_users()
        if not users:
            st.info("No users found.")
        else:
            for u in users:
                st.markdown(f"**{u.get('user_id')} — {u.get('name')}**  \n"
                            f"{u.get('email')} • {u.get('phone')} • role: {u.get('role')}")
    except Exception as e:
        st.error(f"Error fetching users: {e}")

with col_u2:
    st.subheader("Add User")
    with st.form("add_user"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Traveler", "Admin"])
        if st.form_submit_button("Add User"):
            try:
                user = user_service.add_user(name, email, phone, password, role)
                st.success(f"User added (id={user.get('user_id') if user else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to add user: {e}")

st.markdown("---")

# ------------------- BOOKINGS -------------------
st.header("Bookings")
col_b1, col_b2 = st.columns([2, 1])

with col_b1:
    try:
        bookings = booking_service.list_bookings()
        if not bookings:
            st.info("No bookings found.")
        else:
            for b in bookings:
                st.markdown(f"**{b.get('booking_id')}** — user: {b.get('user_id')}  • package: {b.get('package_id')}  \n"
                            f"status: {b.get('status')}  • total: {b.get('total_amount')}  • date: {b.get('booking_date')}")
    except Exception as e:
        st.error(f"Error fetching bookings: {e}")

with col_b2:
    st.subheader("Create Booking")
    with st.form("add_booking"):
        b_user_id = st.number_input("User ID", min_value=1, step=1)
        b_package_id = st.number_input("Package ID", min_value=1, step=1)
        b_status = st.selectbox("Status", ["PLACED", "PENDING", "CANCELLED", "COMPLETED"])
        if st.form_submit_button("Create Booking"):
            try:
                # compute total amount from package if available
                try:
                    pkg = package_service.get_package(int(b_package_id))
                    total_amount = float(pkg.get("price")) if pkg and pkg.get("price") is not None else 0.0
                except Exception:
                    total_amount = 0.0

                booking = booking_service.create_booking(int(b_user_id), int(b_package_id), b_status, float(total_amount))
                st.success(f"Booking created (id={booking.get('booking_id') if booking else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to create booking: {e}")

st.markdown("---")

# ------------------- PAYMENTS -------------------
st.header("Payments")
col_pay1, col_pay2 = st.columns([2, 1])

with col_pay1:
    try:
        payments = payment_service.list_payments()
        if not payments:
            st.info("No payments found.")
        else:
            for p in payments:
                st.markdown(f"**{p.get('payment_id')}** — booking: {p.get('booking_id')}  \n"
                            f"amount: {p.get('amount')}  • status: {p.get('status')}  • date: {p.get('payment_date')}")
    except Exception as e:
        st.error(f"Error fetching payments: {e}")

with col_pay2:
    st.subheader("Record Payment")
    with st.form("add_payment"):
        pay_booking_id = st.number_input("Booking ID", min_value=1, step=1)
        pay_amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        pay_status = st.selectbox("Status", ["SUCCESS", "FAILED", "REFUNDED"])
        if st.form_submit_button("Record Payment"):
            try:
                payment = payment_service.make_payment(int(pay_booking_id), float(pay_amount), pay_status)
                st.success(f"Payment recorded (id={payment.get('payment_id') if payment else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to record payment: {e}")

st.markdown("---")

# ------------------- TRAVEL (ITINERARY & ASSISTANCE) -------------------
st.header("Travel Itineraries & Assistance")
col_t1, col_t2 = st.columns([2, 1])

with col_t1:
    try:
        travels = travel_service.list_travels()
        if not travels:
            st.info("No travel records found.")
        else:
            for t in travels:
                st.markdown(f"**{t.get('travel_id')}** — user: {t.get('user_id')}  • package: {t.get('package_id')}  \n"
                            f"day_plan: {t.get('day_plan')}  \nassistance: {t.get('assistance_notes')}")
    except Exception as e:
        st.error(f"Error fetching travel records: {e}")

with col_t2:
    st.subheader("Add Travel Itinerary")
    with st.form("add_travel"):
        tr_user_id = st.number_input("User ID", min_value=1, step=1)
        tr_package_id = st.number_input("Package ID", min_value=1, step=1)
        tr_day_plan = st.text_area("Day Plan (simple text)")
        tr_assist = st.text_area("Assistance Notes")
        if st.form_submit_button("Add Travel"):
            try:
                travel = travel_service.create_travel(int(tr_user_id), int(tr_package_id), tr_day_plan, tr_assist)
                st.success(f"Travel record added (id={travel.get('travel_id') if travel else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to add travel record: {e}")

st.markdown("---")

# ------------------- REVIEWS -------------------
st.header("Reviews & Feedback")
col_r1, col_r2 = st.columns([2, 1])

with col_r1:
    try:
        reviews = review_service.list_reviews()
        if not reviews:
            st.info("No reviews found.")
        else:
            for r in reviews:
                st.markdown(f"**{r.get('review_id')}** — user: {r.get('user_id')}  • package: {r.get('package_id')}  \n"
                            f"rating: {r.get('rating')}  \ncomment: {r.get('comment')}")
    except Exception as e:
        st.error(f"Error fetching reviews: {e}")

with col_r2:
    st.subheader("Add Review")
    with st.form("add_review"):
        rv_user = st.number_input("User ID", min_value=1, step=1)
        rv_package = st.number_input("Package ID", min_value=1, step=1)
        rv_rating = st.slider("Rating (1-5)", 1, 5, 5)
        rv_comment = st.text_area("Comment")
        if st.form_submit_button("Add Review"):
            try:
                review = review_service.add_review(int(rv_user), int(rv_package), int(rv_rating), rv_comment)
                st.success(f"Review added (id={review.get('review_id') if review else 'unknown'})")
            except Exception as e:
                st.error(f"Failed to add review: {e}")

st.markdown("---")

st.info("Tip: use the CLI (python -m src.cli.main ...) for update/delete operations or extend the Streamlit UI to include edit/delete controls.")
