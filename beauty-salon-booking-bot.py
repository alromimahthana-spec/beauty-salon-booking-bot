# بوت حجز صالون تجميل - ثناء | thanaa.codes

print("=" * 40)
print("💅 صالون ثناء للتجميل - اهلا فيك")
print("=" * 40)

services = {
    "1": ("قص شعر", 80),
    "2": ("صبغة شعر", 150),
    "3": ("استشوار", 60),
    "4": ("مكياج سهرة", 200),
    "5": ("مناكير وبديكير", 90),
    "6": ("تنظيف بشرة", 120),
}

print("\n✨ خدماتنا:")
for key, (name, price) in services.items():
    print(f"{key}. {name} - {price} ريال")

choice = input("\nاختاري رقم الخدمة: ")
service_name, service_price = services.get(choice, ("خدمة غير معروفة", 0))

print(f"\nاخترتي: {service_name} - {service_price} ريال")

print("\n🗓️ الايام المتاحة:")
print("1. السبت")
print("2. الاحد")
print("3. الاثنين")
print("4. الثلاثاء")
print("5. الاربعاء")
print("6. الخميس")

day = input("اختاري اليوم: ")
days = {"1":"السبت","2":"الاحد","3":"الاثنين","4":"الثلاثاء","5":"الاربعاء","6":"الخميس"}
day_name = days.get(day, "غير محدد")

print("\n⏰ الاوقات المتاحة:")
print("1. 10 صباحا")
print("2. 12 ظهرا")
print("3. 2 عصرا")
print("4. 4 عصرا")
print("5. 6 مساء")

time_choice = input("اختاري الوقت: ")
times = {"1":"10 صباحا","2":"12 ظهرا","3":"2 عصرا","4":"4 عصرا","5":"6 مساء"}
time_name = times.get(time_choice, "غير محدد")

print("\n--- بيانات الحجز ---")
name = input("اسمك: ")
phone = input("رقم جوالك: ")

print("\n" + "=" * 40)
print("✅ تم تأكيد حجزك!")
print("=" * 40)
print(f"الاسم: {name}")
print(f"الجوال: {phone}")
print(f"الخدمة: {service_name}")
print(f"اليوم: {day_name}")
print(f"الوقت: {time_name}")
print(f"السعر: {service_price} ريال")
print("\nننتظرك في صالون ثناء 💖")
print("=" * 40)
