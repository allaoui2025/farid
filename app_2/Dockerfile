# استخدام صورة Node.js الأساسية
FROM node:18

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ وتثبيت المتطلبات
COPY package.json package-lock.json ./
RUN npm install

# نسخ باقي ملفات المشروع
COPY . .

# فتح المنفذ 3000 لتطبيق Node.js
EXPOSE 3000

# تشغيل التطبيق عند بدء الحاوية
CMD ["node", "server.js"]
