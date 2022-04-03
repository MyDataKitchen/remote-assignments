function btnCaption() {
    
    let captionText = document.getElementById("caption")

    if (captionText.textContent === 'MyDataKitchen') {
        captionText.textContent = 'Have a Good Time!';
    } else {
        captionText.textContent = 'MyDataKitchen';
    }


}

function btnShowMore() {
    
    let moreInfo = document.getElementsByClassName("show-more");
    let btnText = document.getElementsByClassName("button");
  
    if (moreInfo[0].style.display === "inline") {
        
        btnText[0].innerHTML = "SHOW MORE"; 
        moreInfo[0].style.display = "none";
    } else {
        
        btnText[0].innerHTML = "SHOW LESS"; 
        moreInfo[0].style.display = "inline";
    }
  }