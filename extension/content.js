console.log('[Depolarize] contentScript running on', location.href);

let paras = Array.from(document.querySelectorAll('article p'));
console.log('[Depolarize] <article><p> count:', paras.length);

if (!paras.length) {
    paras = Array.from(document.body.querySelectorAll('p'));
    console.log('[Depolarize] fallback <body><p> count:', paras.length);
}

let text;
if (paras.length) {
    text = paras.map(p => p.innerText).join('\n\n');
} else {
    text = document.body.innerText;
    console.log('[Depolarize] no <p> tags at all, sending entire body text (length:', text.length, 'chars )');
}

console.log('[Depolarize] sending text to background…');
chrome.runtime.sendMessage({ type: 'PAGE_TEXT', payload: text });
