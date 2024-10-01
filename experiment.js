// <!DOCTYPE html>
// <html lang="uz">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Rang O'zgarishi</title>
//     <style>
//         body { transition: background-color 0.5s; }
//     </style>
// </head>
// <body>
//     <button id="changeColor">Rangni o'zgartirish</button>
//     <script>
//         const button = document.getElementById('changeColor');
//         button.addEventListener('click', () => {
//             const randomColor = `#${Math.floor(Math.random()*16777215).toString(16)}`;
//             document.body.style.backgroundColor = randomColor;
//         });
//     </script>
// </body>
// </html>
// <!DOCTYPE html>
// <html lang="uz">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Kalkulyator</title>
// </head>
// <body>
//     <input id="num1" type="number" placeholder="Birinchi son">
//     <input id="num2" type="number" placeholder="Ikkinchi son">
//     <button id="add">Qo'shish</button>
//     <p id="result">Natija: </p>
//     <script>
//         const button = document.getElementById('add');
//         button.addEventListener('click', () => {
//             const num1 = parseFloat(document.getElementById('num1').value);
//             const num2 = parseFloat(document.getElementById('num2').value);
//             const result = num1 + num2;
//             document.getElementById('result').innerText = `Natija: ${result}`;
//         });
//     </script>
// </body>
// </html>
// <!DOCTYPE html>
// <html lang="uz">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>So'z Generatori</title>
// </head>
// <body>
//     <button id="generateWord">Yangi so'z olish</button>
//     <p id="word"></p>
//     <script>
//         const words = ['javascript', 'dasturlash', 'o'yin', 'kompyuter', 'internet'];
//         const button = document.getElementById('generateWord');
//         button.addEventListener('click', () => {
//             const randomIndex = Math.floor(Math.random() * words.length);
//             document.getElementById('word').innerText = words[randomIndex];
//         });
//     </script>
// </body>
// </html>
// experiment