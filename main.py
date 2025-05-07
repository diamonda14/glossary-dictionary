glossary = {}

def add\_term():
term = input("🔤 أدخل المصطلح: ")
meaning = input("📝 أدخل الشرح: ")
glossary\[term] = meaning
print(f"✅ '{term}' تمت إضافته بنجاح!\n")

def show\_glossary():
if not glossary:
print("📭 لا توجد مصطلحات بعد.\n")
else:
print("📚 قائمة المصطلحات:")
for term, meaning in glossary.items():
print(f"🔸 {term}: {meaning}")
print()

def search\_term():
term = input("🔍 أدخل المصطلح للبحث عنه: ")
if term in glossary:
print(f"🔎 {term} ➜ {glossary\[term]}\n")
else:
print("❌ المصطلح غير موجود.\n")

while True:
print("=== 🧠 قاموس بايثون التفاعلي ===")
print("1. ➕ إضافة مصطلح")
print("2. 📖 عرض جميع المصطلحات")
print("3. 🔍 البحث عن مصطلح")
print("4. 🚪 خروج")

```
choice = input("➡️ اختر رقم العملية: ")

if choice == "1":
    add_term()
elif choice == "2":
    show_glossary()
elif choice == "3":
    search_term()
elif choice == "4":
    print("👋 إلى اللقاء!")
    break
else:
    print("❗ اختيار غير صالح.\n")
```
