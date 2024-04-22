const URL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
var currentCount = 13;

/**
 * fetch data from the specified URL and render spot information based on startIndex
 * @param {Number} startIndex The start index of spots to render
 * @param {Number} count The number of spots to render
 */
function getData(startIndex, count){
    fetch(URL)
        .then(function(response) {
            return response.json(); 
        })
        .then(function(resp) {
            let results = resp.data.results;
            
            
        for (let i=startIndex; i<startIndex+count;i++){
            if (i>=results.length) {
                let loadMoreButton = document.querySelector("#load");
                loadMoreButton.style.display = "none";
                return;
            }
            let result =results[i]
            let className = determineClassName(i);

            appendSpot(result,className)

            }
        if (startIndex!==0)currentCount += count;
        
        });
}
/**
 * Determine the className based on the current viewport width and index
 * @param {number} i The index of spots
 * @returns The determined className
 */
function determineClassName(i){
    const width = window.innerWidth;
    if (width >600 && width <=1200){
        if (i<2) {
            return 'sb';
        } else if (i===2) {
            return 'sb2';
        } else if ((i%10===1)||(i%10===2)) {
            return 'lb';
        } else {
            return 'mb';
        }
    // console.log("601px < width <=1200px")
    } else{
        if (i<3) {
            return 'sb';
        }else if((i===3) || (i-3)%5===0){
            return 'lb';
        }else{
            return 'mb';
        }
    // console.log("其他範圍")
    }
}

/**
 * Render the spot names and pictures to divs
 * @param {list} result The fetched data of spots
 * @param {str} className The determined clasName for styling
 */
function appendSpot(result,className){

    let parentDiv = document.createElement('div');
    parentDiv.className = className;
    

    let spotImage = document.createElement('img');
    spotImage.src = "https://" + result.filelist.split("https://")[1];


    parentDiv.appendChild(spotImage);


    let spotName = document.createElement('div');
    spotName.textContent = result.stitle;


    parentDiv.appendChild(spotName);

    if(className === "lb"|| className === "mb"){
        let starImage = document.createElement('img');
        starImage.src = "star1.png";
        starImage.className = "star";
        parentDiv.appendChild(starImage);
    }


    let container = document.querySelector(".content .container");
    container.appendChild(parentDiv);
    
}

window.addEventListener('resize', function() {
    let container = document.querySelector(".content .container");
    container.innerHTML = '';
    getData(0, currentCount);
});

document.addEventListener('DOMContentLoaded',function(){
    getData(0,currentCount);
});

let loadMoreButton = document.querySelector('#load')
loadMoreButton.addEventListener('click',function() {
    let newCount = 10;
    getData(currentCount,newCount);
});