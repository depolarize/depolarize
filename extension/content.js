console.log('[De‑Polarize] contentScript running on', location.href);

// Try grabbing article text first…
let paras = Array.from(document.querySelectorAll('article p'));
console.log('[De‑Polarize] <article><p> count:', paras.length);

// Fallback to body paragraphs if none found
if (!paras.length) {
    paras = Array.from(document.body.querySelectorAll('p'));
    console.log('[De‑Polarize] fallback <body><p> count:', paras.length);
}

// Ultimate fallback: send the whole body text
let text;
if (paras.length) {
    text = paras.map(p => p.innerText).join('\n\n');
} else {
    text = document.body.innerText;
    console.log('[De‑Polarize] no <p> tags at all, sending entire body text (length:', text.length, 'chars )');
}

console.log('[De‑Polarize] sending text to background…');
chrome.runtime.sendMessage({ type: 'PAGE_TEXT', payload: text });
