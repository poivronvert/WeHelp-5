const URL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
let currentCount = 13;

function getData(startIndex, count){
    fetch(URL)
        .then(function(response) {
            return response.json(); //解析成一個json物件
        })
        .then(function(resp) {
            let results = resp.data.results;
            console.log(results.legth)
            
        for (let i=startIndex; i<startIndex+count;i++){
            if (i>=results.legth) {
                let loadMoreButton = document.querySelector("#load");
                loadMoreButton.style.display = "none";
                break;
            }
            let result =results[i]
            let className = (i < 3) ? "sb" : ((i%5===3 && i<=13) ||((i-3)%5===3 && i>13)) ? "lb" : "mb";
            appendSpot(result,className)
            }
        currentCount += count;
        });
}

function appendSpot(result,className){
    //創建包含圖片和景點名稱的父容器div，並套用class
    let parentDiv = document.createElement('div');
    parentDiv.className = className;
    
    // 創建圖片元素
    let spotImage = document.createElement('img');
    spotImage.src = "https://" + result.filelist.split("https://")[1];

    //添加到父容器中
    parentDiv.appendChild(spotImage);

    //創建景點名稱元素
    let spotName = document.createElement('div');
    spotName.textContent = result.stitle;

    //添加到父容器中
    parentDiv.appendChild(spotName);

    if(className === "lb"|| className === "mb"){
        let starImage = document.createElement('img');
        starImage.src = "star1.png";
        starImage.className = "star";
        parentDiv.appendChild(starImage);
    }

    // 將父容器添加到容器中
    let container = document.querySelector(".content .container");
    container.appendChild(parentDiv);
}


document.addEventListener('DOMContentLoaded',function(){
    getData(0,currentCount);

    let loadMoreButton = document.querySelector('#load');
        loadMoreButton.addEventListener('click',function() {
            let newCount = 10;
            getData(currentCount,newCount);
    });

});