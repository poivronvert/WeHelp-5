function check() {
    if (document.getElementById("consent").checked) {
        return true;
    }else{
        alert("Please check the checkbox first");
        return false;
    }
}


function confirmDelete(button) {
    const messageId = button.getAttribute('messageid');
    const confirmed = confirm(`確定要刪除該留言嗎？`);
    if (confirmed) {
        try{
            deleteMsg(messageId)
        }catch(error){
            console.log(error)
        }
    }
}

function deleteMsg(messageId) {
    const data = {
        message_id: messageId
    };
    fetch('/deleteMessage',{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body: JSON.stringify(data),
    }).then(resp=>{
        if(resp.status == 200){
            alert(`刪除成功`)
            location.reload();
        }else if (resp.status==304){
            alert(`Nothing Modified.`)
        };
    }).catch(error=>{
        throw error
    })

}

