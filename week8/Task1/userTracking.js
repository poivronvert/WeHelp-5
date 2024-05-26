console.time()

function userTracking(){
    let startTime = Date.now();
    window.addEventListener("unload", function() {
        let duration = Date.now() - startTime;
        console.log(`User has been on the site for ${duration} milliseconds`);
    });
    }




userTracking();


console.timeEnd()