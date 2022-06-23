let miniDisplay = document.getElementById('screen');
let ansDisplay = document.getElementById('result');
let buttonPress = document.querySelectorAll('.btn');
console.log(buttonPress);
let screenValue = '';
let isEndEq = false;

for (item of buttonPress) {
    item.addEventListener('click', (e) => {

        let buttonText = e.target.innerText;
        console.log('buttonText: ', buttonText);

       
        if (buttonText == "AC"){

            screenValue = "";
            ansDisplay.value = screenValue;
            miniDisplay.value = screenValue;
            isEndEq = false;
        }
        else if (buttonText == "DEL"){
            
            screenValue = screenValue.slice(0,-1);
            ansDisplay.value = screenValue;
            isEndEq = false;

        }
        else if (buttonText == 'x'){
            buttonText = '*';
            screenValue += buttonText;
            ansDisplay.value = screenValue;
            isEndEq = false;
        }
        else if (buttonText == "="){
            miniDisplay.value = screenValue;
            ansDisplay.value = eval(screenValue);
            screenValue = ansDisplay.value;
            isEndEq = true;
        }
        else{
            if(((buttonText >= '0' && buttonText <='9') || buttonText== "00" || buttonText== ".") && isEndEq == true){
                screenValue = "";
                miniDisplay.value = screenValue;
                ansDisplay.value = screenValue;
                isEndEq = false;
            }
            
            screenValue+= buttonText;
            ansDisplay.value = screenValue;
            isEndEq = false;
            
        }
    })
}