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
                if (i==results.length) {
                    let loadMoreButton = document.querySelector("#load");
                    loadMoreButton.style.display = "none";
                    break;
                }
                let result =results[i]
                if (i <3){
                    appendSpot(result,".first3Spots")
                }else{
                    appendSpot(result,".otherSpots")
                }

                }
            if (startIndex!==0)currentCount += count;
        });
}

/**
 * Render the spot names and pictures to divs
 * @param {list} result The fetched data of spots
 * @param {str} className The determined clasName for styling
 */
function appendSpot(result,place){

    let parentDiv = document.createElement('div');
    parentDiv.className = "spot";
    
    
    let spotImage = document.createElement('img');
    spotImage.src = "https://" + result.filelist.split("https://")[1];
    parentDiv.appendChild(spotImage);

    let spotName = document.createElement('div');
    spotName.textContent = result.stitle;
    parentDiv.appendChild(spotName);

    if (place == ".otherSpots"){ 
        let starImage = document.createElement('img');
        starImage.src = "star1.png";
        starImage.className = "star";
        parentDiv.appendChild(starImage);
    }

    let container = document.querySelector(place);
    container.appendChild(parentDiv);
    
}

document.addEventListener('DOMContentLoaded',function(){
    getData(0,currentCount);
});

let loadMoreButton = document.querySelector('#load')
loadMoreButton.addEventListener('click',function() {
    let newCount = 10;
    getData(currentCount,newCount);
});