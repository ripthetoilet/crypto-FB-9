let alpha = {
  й: 0,
  ц: 0,
  у: 0,
  к: 0,
  е: 0,
  н: 0,
  г: 0,
  ш: 0,
  щ: 0,
  з: 0,
  х: 0,
  ф: 0,
  ы: 0,
  в: 0,
  а: 0,
  п: 0,
  р: 0,
  о: 0,
  л: 0,
  д: 0,
  ж: 0,
  э: 0,
  я: 0,
  ч: 0,
  с: 0,
  м: 0,
  и: 0,
  т: 0,
  ь: 0,
  б: 0,
  ю: 0,
  " ": 0,
};

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
    let keys = ["шо", "там", "делают", "москали", "чтомненаписать"];
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
  for (let letter of text) {
    for (let key in alpha) {
      if (key == letter) {
        alpha[letter]++;
      }
    }
  }
  let specInd = 0;
  for (i in alpha) {
    specInd += alpha[i] * (alpha[i] - 1);
  }
  specInd /= text.length * text.length - 1;
  return specInd;
}
