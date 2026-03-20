# السلسلة كما هي
binary_bits = [0,1,0,1,0,1,1,0,0,0,0,0,1]

# متغيرات لحساب العدد (كما طلب السؤال)
positive_changes = 0
negative_changes = 0

# حلقة التكرار: نستخدم range لنحصل على الموقع i
# ملاحظة مهمة: نستخدم len() - 1 لأننا سنقارن مع العنصر التالي
# لو وصلنا لآخر عنصر، لا يوجد شيء بعده، لذا نتوقف قبله بخطوة
for i in range(len(binary_bits) - 1):
    
    # نقارن العنصر الحالي [i] مع العنصر التالي [i+1]
    
    # 1. حالة الصعود (إيجابي): الحالي 0 والتالي 1
    if binary_bits[i] == 0 and binary_bits[i+1] == 1:
        positive_changes += 1 # نزيد العداد
        
    # 2. حالة الهبوط (سلبي): الحالي 1 والتالي 0
    elif binary_bits[i] == 1 and binary_bits[i+1] == 0:
        negative_changes += 1 # نزيد العداد

# طباعة النتيجة النهائية
print("Positive changes:", positive_changes)
print("Negative changes:", negative_changes)