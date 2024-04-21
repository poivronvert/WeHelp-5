const URL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
var currentCount = 13;
/**
 * fetch url and get spot info; define class type for small, medium, large picture
 * @param {Number} startIndex determin the start index of spots to render 
 * @param {Number} count determin the start index of spots to render 
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
            let className = '';
            if (i<3) {
                className = 'sb';
            }else if((i===3) || (i-3)%5===0){
                className = 'lb';
            }else{
                className = 'mb';
            }
        
            appendSpot(result,className)

            }
        if (startIndex!==0)currentCount += count;
        
        });
}
/**
 * render the spot names and pictures to divs
 * @param {list} result fetched data
 * @param {str} className defined style to apply
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


document.addEventListener('DOMContentLoaded',function(){
    getData(0,currentCount);

});
let loadMoreButton = document.querySelector('#load')
loadMoreButton.addEventListener('click',function() {
    let newCount = 10;
    getData(currentCount,newCount);
});