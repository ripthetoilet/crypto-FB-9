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
  let alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
  let dictionaryObj={}
  let revDicObj={}
  for (let i=0; i<alphabet.length; i++){
    dictionaryObj[i]=alphabet[i]
    revDicObj[alphabet[i]]=i
  }
console.log(dictionaryObj);
  /*   console.log(revDicObj); */
  let readyText

  document.querySelector("#encrypt").addEventListener("click", function () {
    let file = document.getElementById("file1").files[0];
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function () {
        readyText=textEditor(reader.result)
    }
    reader.onerror = function () {
      console.log(reader.error);
    };
  });

  document.querySelector("#decrypt").addEventListener("click", function () {
    let file = document.getElementById("file2").files[0];
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function () {
      let decText=decryptText(reader.result ,findKey(reader.result, readyText, alpha), 16)
       let str=""
       for(let i=0; i<decText.length; i++){
       
        str+=decText[i]
        if (str.length==16){
          console.log(str);
          str=""
        }
        
      }
    };
    reader.onerror = function () {
      console.log(reader.error);
    };
  });

  function textEditor(text) {
    let editText;
    editText = text.replace(/[!-@]|[\[-`]|[\{-~]|I|—|…|»|’|[a-z]|«/gi, "").toLowerCase().replace(/  /gi, " ").replace(/ё/gi, "e").replace(/ъ/gi, "ь");
    return editText;
  }

  function meanValue(arr){
      let sum=0;
      for (let value of arr){
        sum+=value
      }
      return sum/arr.length
  }

  function specialIndex(obj, text) {
    let specInd = 0;
    for (i in obj) {
      specInd += obj[i] * (obj[i] - 1);
    }
    specInd /= text.length * text.length - 1;
    return specInd;
  }

  function findKey(encText, text, alpha){
      let mathSpecInd=0;
      let letterFrq={}
      for (let letter of text) {
        for (let key in alpha) {
          if (key == letter) {
            alpha[letter]++;
          }
        }
      }
      for (let key in alpha){
          alpha[key]/=text.length
          mathSpecInd+=Math.pow(alpha[key], 2)
      }
      /* console.log("mathSpecInd " +mathSpecInd); */
      let checkDct={}
      for (let r=2;r<33;r++){
          let arr=[]
          
          for (let j=0; j<r;j++){
              let strTmp="";
              for (let i=j; i<encText.length;i+=r){
                  strTmp+=encText[i]
              }
              letterFrq={}
              for (let i = 0; i < strTmp.length; i++) {
                if (letterFrq[strTmp[i]] != undefined) letterFrq[strTmp[i]]++;
                else letterFrq[strTmp[i]] = 1;
              }
              arr.push(specialIndex(letterFrq,strTmp))
          }
          
          checkDct[r]=meanValue(arr)
          /* console.log("arr");
          console.log(arr); */
      }
      
      for (let key in checkDct){
        checkDct[key]=Math.abs(checkDct[key]-mathSpecInd)
      }
      /* console.log("checkDct");
      console.log(checkDct); */
      let minValue=1;
      let minValKey;
      for (let key in checkDct){
        if (checkDct[key]<minValue) {
          minValue=checkDct[key]
          minValKey=key
        }
      }
      let keyStr="";

      /* console.log("minval "+minValue);
      console.log("minValKey "+minValKey); */
      for (let i=0; i<minValKey; i++){
          let tmpArr=[]
          let blocksObj={}
          for (let j=i; j<encText.length; j+=parseInt(minValKey)){
              //console.log(encText[j]);
              tmpArr.push(encText[j])
          } 
          blocksObj={}
          for (let i = 0; i < tmpArr.length; i++) { 
            if (blocksObj[tmpArr[i]] != undefined) blocksObj[tmpArr[i]]++;
            else blocksObj[tmpArr[i]] = 1;
          }
          /* console.log("blocksObj");
          console.log(blocksObj); */
          let popular =0;
          let popularKey
          for (let key in blocksObj){
            if (blocksObj[key]>popular) {
              popular=blocksObj[key]
              popularKey=key
            }
          }
          /* console.log("popolar "+popular);
          console.log("popularKey "+popularKey); */
          
          keyStr+=dictionaryObj[(Math.abs(revDicObj[popularKey]-14))%32]
          /* console.log(keyStr); */
      }
      /* console.log(keyStr); */
      return keyStr
  } 
  function decryptText(encText, key, keyValue){
    let mt=[]
    key="делолисоборойдей"
    console.log(key);
    for (let i=0; i<encText.length; i++){
      let par1=alphabet.indexOf(encText[i])
      let par2=alphabet.indexOf(key[i%key.length])
      mt.push(alphabet[(par1-par2)%alphabet.length])
    }
    return mt.join("");
  }