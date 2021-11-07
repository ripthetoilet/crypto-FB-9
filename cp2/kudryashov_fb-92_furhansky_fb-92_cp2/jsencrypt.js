let alpha = {};

let alphstr = "йцукенгшщзхэждлорпавыфячсмитьбю";

function textEditor(text) {
  let editText;
  editText = text.replace(/[!-@]|[\[-`]|[\{-~]|I|—|…|»|’|[a-z]|«/gi, "").toLowerCase().replace(/  /gi, " ").replace(/ё/gi, "e").replace(/ъ/gi, "ь");
  return editText;
}

document.querySelector("#encrypt").addEventListener("click", function () {
  let file = document.getElementById("file1").files[0];
  let reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function () {
    let keys = ["йц","уке","нгшщ","зхфыи","вапролджєя","чсмитьбюфыв","йфяцычувскам","ипенртьогшлбщ","йцукенрпавыфяч","ячсмитьбюфывапр","йысаертьлщшгроне","йфывмсапрнкеготри","йцывукаепрнроггшол", "лшгнепротимсакувчыц", "ячспролдбьтименпауке"];
    let ulList = document.createElement("ul");
    for (let key of keys) {
      let editText=encrypt(textEditor(reader.result), key);
      let liEl = document.createElement("li");
      liEl.classList.add("keyLength:" + key.length);
      liEl.textContent = editText
      ulList.append(liEl);
      console.log("keyLength: " + key.length + " accordence index: "+ specialIndex(editText, key));
    }
    
    document.querySelector(".uls").append(ulList);
  };
  reader.onerror = function () {
    console.log(reader.error);
  };
});

/* document.querySelector("#decrypt").addEventListener("click", function () {
  let file = document.getElementById("file2").files[0];
  let reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function () {};
  reader.onerror = function () {
    console.log(reader.error);
  };
}); */

function encrypt(text, key) {
  let arrayNum = [];
  for (let i = 0; i < text.length; i++) {
    let par1 = alphstr.indexOf(text[i]);
    let par2 = alphstr.indexOf(key[i % key.length]);
    arrayNum.push((alphstr[(par1 + par2)% alphstr.length]) );
  }
  return arrayNum.join("");
}

function specialIndex(text) {
  alpha={}
  for (let i = 0; i < text.length; i++) { 
    if (alpha[text[i]] != undefined) alpha[text[i]]++;
    else alpha[text[i]] = 1;
  }
  let specInd = 0;
  for (i in alpha) {
    specInd += alpha[i] * (alpha[i] - 1);
  }
  specInd /= text.length * text.length - 1;
  return specInd;
}
