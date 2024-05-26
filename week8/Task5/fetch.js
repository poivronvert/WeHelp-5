document.getElementById('submitToGoogle').addEventListener('click', function() {
    let message = document.getElementById('message').value; //message 變量需要在點擊事件處理器內部重新獲取
    //const url = new URL(`https://jsonplaceholder.typicode.com/posts?message=${encodeURIComponent(message)}`);
    const url = new URL(`https://www.google.com/?message=${encodeURIComponent(message)}`); //GET 請求的參數放在 URL 中

    fetch(url)
        .then(response => {
            if (!response.ok) {
                console.log('無法連線');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        }).catch(error => {
            console.error('發生錯誤:', error);
        });
});

document.getElementById('submitToJSON').addEventListener('click', function() {
    //let message = document.getElementById('message').value;
    //const url = new URL(`https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json/?message=${encodeURIComponent(message)}`);
    const url = new URL('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json');

    fetch(url)
        .then(response => {
            if (!response.ok) {
                console.log('無法連線');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        }).catch(error => {
            console.error('發生錯誤:', error);
        });
});