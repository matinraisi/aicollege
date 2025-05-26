const dialogQuestions = [  
    {   
        question: "اسم شما چیست؟",   
        correctAnswer: "علی",   
        correctResponse: "پاسخ درست: علی"   
    },  
    {   
        question: "چند سال دارید؟",   
        correctAnswer: "25",   
        correctResponse: "پاسخ درست: 25"   
    },  
    {   
        question: "شغل شما چیست؟",   
        correctAnswer: "برنامه‌نویس",   
        correctResponse: "پاسخ درست: برنامه‌نویس"   
    },  
    {   
        question: "کدام کشور را دوست دارید؟",   
        correctAnswer: "ایران",   
        correctResponse: "پاسخ درست: ایران"   
    },  
];  

let currentDialogQuestionIndex = 0;  
let isRecording = false; // متغیر برای وضعیت ضبط گفتگو  

document.getElementById("startDialogButton").addEventListener("click", () => {  
    if (!isRecording) {  
        // اگر در حال ضبط نیستیم، مکالمه را شروع کنیم  
        isRecording = true; // تنظیم وضعیت ضبط  
        currentDialogQuestionIndex = 0; // بازنشانی اندیس سوال  
        document.getElementById("dialogResponses").innerText = ""; // پاک کردن پاسخ‌های قبلی  
        document.getElementById("startDialogButton").innerText = "مکالمه در حال ضبط است..."; // تغییر متن دکمه  
        askDialogQuestion();  
    } else {  
        // اگر در حال ضبط هستیم، مکالمه را متوقف کنیم  
        isRecording = false; // تنظیم وضعیت ضبط به صورت غیر فعال  
        currentDialogQuestionIndex = 0; // بازنشانی اندیس سوال  
        document.getElementById("dialogResponses").innerText = ""; // پاک کردن پاسخ‌های قبلی  
        document.getElementById("dialogQuestion").innerText = "سوال: معلم، سوالی بپرس."; // بازگشت به حالت اولیه  
        document.getElementById("startDialogButton").innerText = "شروع مکالمه"; // تغییر متن دکمه  
        document.getElementById("dialogProgressBar").value = 0; // نوار پیشرفت به حالت اولیه  
        document.getElementById("dialogProgressText").innerText = "سوال 1 از 4"; // به روز رسانی متن نوار پیشرفت  
    }  
});  

function askDialogQuestion() {  
    if (currentDialogQuestionIndex < dialogQuestions.length) {  
        const currentDialogQuestion = dialogQuestions[currentDialogQuestionIndex].question;  
        document.getElementById("dialogQuestion").innerText = `سوال: ${currentDialogQuestion}`;  
        speak(currentDialogQuestion); // فعال‌سازی قابلیت مکالمه صوتی  
        updateDialogProgressBar(); // به‌روزرسانی نوار پیشرفت  
    } else {  
        document.getElementById("dialogQuestion").innerText = "مکالمه تمام شد. به شما تبریک می‌گوییم!";  
        document.getElementById("dialogResponses").innerText = ""; // پاک کردن پاسخ‌ها  
        isRecording = false; // حالت ضبط را غیر فعال می‌کنیم  
        document.getElementById("startDialogButton").innerText = "شروع مکالمه"; // بازگرداندن متن دکمه  
    }  
}  

function updateDialogProgressBar() {  
    const progress = ((currentDialogQuestionIndex + 1) / dialogQuestions.length) * 100; // محاسبه درصد پیشرفت  
    document.getElementById("dialogProgressBar").value = progress;  
    document.getElementById("dialogProgressText").innerText = `سوال ${currentDialogQuestionIndex + 1} از ${dialogQuestions.length}`; // به‌روزرسانی شماره سوال  
}  

function speak(text) {  
    // اینجا می‌توانید کد مربوط به تبدیل متن به صدا را اضافه کنید  
    console.log(text); // برای شبیه‌سازی  
}  

function checkAnswer(userAnswer) {  
    const currentDialogQuestion = dialogQuestions[currentDialogQuestionIndex];  
    if (userAnswer.trim() === currentDialogQuestion.correctAnswer) {  
        document.getElementById("dialogResponses").innerText = "پاسخ شما درست است!";  
        currentDialogQuestionIndex++;  
        askDialogQuestion();  
    } else {  
        document.getElementById("dialogResponses").innerText = "پاسخ شما اشتباه است.";  
    }  
}  

// فرض بر این است که یک تابع برای پردازش پاسخ کاربر اضافه می‌شود  
// به عنوان مثال، با استفاده از API مکالمه صوتی، پاسخ کاربر را دریافت کنید و به تابع checkAnswer بفرستید  