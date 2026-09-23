#E-Commerce Discount & Free Shipping

cart_total = 50.99
is_vip = True
is_guest = False
promo_code = "SAVE10"
if cart_total >= 50 or is_vip:
    print("Free shipping")
else:
    print("You have to pay for shipping")


if promo_code and not is_guest:
    discaunt = cart_total * 0.10
    final_total = cart_total - discaunt
    print("10% discount applied")
    print(f"Final total: {final_total:.2f}")
else:
    print("Discaunt is not applied")
    print(f"Final total: {cart_total}")

