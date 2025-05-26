//////////////////////// لغات  ///////////////////////////////////////////////

const words = [
    { word: "book", image: "./assets/images/images.png", translation: "کتاب" },
    { word: "pen", image: "pen.jpg", translation: "خودکار" },
    { word: "apple", image: "apple.jpg", translation: "سیب" },
    { word: "car", image: "car.jpg", translation: "خودرو" }
];

let currentIndex = 0;

const wordDisplay = document.getElementById("word-display");
const wordImage = document.getElementById("word-image");
const statusMessage = document.getElementById("status-message");
const progressBar = document.getElementById("progress");
const translation = document.getElementById("translation");
const pronounceButton = document.getElementById("pronounce-button");
const startSpeechButton = document.getElementById("start-speech-button");
const showTranslationButton = document.getElementById("show-translation-button");

// بارگذاری کلمه اولیه
function loadWord() {
    const currentWord = words[currentIndex];
    wordDisplay.textContent = currentWord.word;
    wordImage.src = currentWord.image;
    translation.textContent = `ترجمه: ${currentWord.translation}`;
    translation.classList.remove("active");
}

loadWord();

// تلفظ کلمه توسط سیستم
pronounceButton.addEventListener("click", () => {
    const utterance = new SpeechSynthesisUtterance(words[currentIndex].word);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);

    utterance.onend = () => {
        statusMessage.textContent = "می‌توانید تلفظ خود را شروع کنید!";
        startSpeechButton.classList.remove("hidden"); // نمایش دکمه "شروع تلفظ"
    };
});

// نمایش ترجمه کلمه با استایل بهتر
showTranslationButton.addEventListener("click", () => {
    translation.classList.toggle("active");
});

// تشخیص تلفظ کاربر
startSpeechButton.addEventListener("click", () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = (event) => {
        const userSpeech = event.results[0][0].transcript.trim().toLowerCase();
        if (userSpeech === words[currentIndex].word) {
            statusMessage.textContent = "آفرین! تلفظ صحیح است.";
            currentIndex++;
            if (currentIndex < words.length) {
                loadWord();
                progressBar.style.width = `${(currentIndex / words.length) * 100}%`;
                startSpeechButton.classList.add("hidden");
            } else {
                progressBar.style.width = "100%";
                statusMessage.textContent = "تبریک! شما تمام لغات را یاد گرفتید.";
            }
        } else {
            statusMessage.textContent = "تلفظ صحیح نیست، دوباره تلاش کنید.";
        }
    };
});

//////////////////////// مکالمه  ///////////////////////////////////////////////

let conversation = [];
let currentConversationIndex = 0;
let selectedVoiceType = "female"; 
let playbackSpeed = 1.0;

const uploadImageInput = document.getElementById("upload-image");
const conversationText = document.getElementById("conversation-text");
const startInteractionButton = document.getElementById("start-interaction-button");
const voiceTypeSelect = document.getElementById("voice-type");
const speedOptionsSelect = document.getElementById("speed-options");
const confirmOptionsButton = document.getElementById("confirm-options");

let voices = [];
window.speechSynthesis.onvoiceschanged = () => {
    voices = window.speechSynthesis.getVoices();
};

confirmOptionsButton.addEventListener("click", () => {
    selectedVoiceType = voiceTypeSelect.value;
    playbackSpeed = parseFloat(speedOptionsSelect.value);
    alert(`تنظیمات اعمال شد: ${selectedVoiceType === 'female' ? 'زن' : 'مرد'} | سرعت: ${playbackSpeed}x`);
});

uploadImageInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) {
        Tesseract.recognize(file, 'eng').then(({ data: { text } }) => {
            conversation = parseConversationFromText(text);
            alert("متن با موفقیت استخراج شد!");
            conversationText.innerHTML = "<strong>مکالمه آماده است. روی Start Interaction کلیک کنید!</strong>";
            startInteractionButton.style.display = "block";
        }).catch((error) => {
            console.error("خطا در استخراج متن از تصویر:", error);
            alert("متن استخراج نشد. لطفاً دوباره امتحان کنید.");
        });
    }
});

function parseConversationFromText(text) {
    const lines = text.split('\n').filter(line => line.trim() !== '');
    return lines.map((line) => {
        const [speaker, ...message] = line.split(':');
        return { speaker: speaker.trim(), text: message.join(':').trim() };
    });
}

startInteractionButton.addEventListener("click", () => {
    if (conversation.length === 0) {
        alert("هیچ مکالمه‌ای برای نمایش وجود ندارد.");
        return;
    }
    currentConversationIndex = 0;
    conversationText.innerHTML = '';
    proceedToInteractiveConversation();
});

function proceedToInteractiveConversation() {
    if (currentConversationIndex < conversation.length) {
        const line = conversation[currentConversationIndex];
        conversationText.innerHTML += `<strong>${line.speaker}:</strong> ${line.text}<br>`;
        currentConversationIndex++;

        // خواندن خط به خط مکالمه
        const utterance = new SpeechSynthesisUtterance(line.text);
        utterance.lang = 'en-US';
        utterance.rate = playbackSpeed;
        utterance.voice = selectedVoiceType === "female"
            ? voices.find(voice => voice.name.includes("Female"))
            : voices.find(voice => voice.name.includes("Male"));

        speechSynthesis.speak(utterance);

        utterance.onend = () => {
            proceedToInteractiveConversation();
        };
    } else {
        conversationText.innerHTML += "<strong>مکالمه پایان یافت!</strong>";
        alert("مکالمه به پایان رسید!");
    }
}

