function check() {
    if (document.getElementById("consent").checked) {
        return true;
    }else{
        alert("Please check the checkbox first");
        return false;
    }
}


function confirmDelete(button) {
    const messageId = button.getAttribute('messageId');
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

function editShowHidden(messageId) {
    let editButtonToHide = document.getElementById('editButton_'+messageId);
    let editableToHide = document.getElementById('editable_'+messageId);
    let deleteButtonToHide = document.getElementById('deleteButton_'+messageId)
    let editingToShow = document.getElementById('editing_'+messageId);
    let editConfirmButtonToShow = document.getElementById('editConfirmButton_'+messageId);
    let cancelButtonToShow = document.getElementById('cancelButton_'+messageId);
    if (editButtonToHide) {
        editButtonToHide.style.display="none";
        editableToHide.style.display="none";
        deleteButtonToHide.style.display="none";
        editingToShow.style.display="inline-block";
        editConfirmButtonToShow.style.display="inline-block";
        cancelButtonToShow.style.display="inline-block";
    }
}

function cancelEdit(messageId) {
    let editButtonToHide = document.getElementById('editButton_'+messageId);
    let editableToHide = document.getElementById('editable_'+messageId);
    let deleteButtonToHide = document.getElementById('deleteButton_'+messageId)
    let editingToShow = document.getElementById('editing_'+messageId);
    let editConfirmButtonToShow = document.getElementById('editConfirmButton_'+messageId);
    let cancelButtonToShow = document.getElementById('cancelButton_'+messageId);
    if (editButtonToHide) {
        editButtonToHide.style.display="inline-block";
        editableToHide.style.display="inline-block";
        deleteButtonToHide.style.display="inline-block";
        editingToShow.style.display="none";
        editConfirmButtonToShow.style.display="none";
        cancelButtonToShow.style.display="none";
    }
}

function editMsg(messageId) {
    const editElement = document.getElementById('editing_'+messageId);
    const editedContent = editElement.value;
    const data = {
        message_id: messageId,
        content: editedContent,
    };
    fetch('/editMessage',{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body: JSON.stringify(data),
    }).then(resp=>{
        if(resp.status == 200){
            alert(`修改成功`)
            location.reload();
        }else if (resp.status==304){
            alert(`Nothing Modified.`)
        };
    }).catch(error=>{
        throw error
    })

}

function queryName() {
    const queryElement = document.getElementById('queryName')

    const q_Name = queryElement.value

    fetch(`/api/member/?username=${q_Name}`)
    .then(resp=> {
        if (!resp.ok){
            throw new Error('Network response was not ok');
        }
        return resp.json();
    })
    .then(data=> {
        if(data.data===null){
            const divElement = document.getElementById('showName'); 
            divElement.innerHTML=`
            <div>No Data</div>`;
        } else{
        const name = data.data.name;
        const username = data.data.username;
        const divElement = document.getElementById('showName');
        divElement.innerHTML=`
            <div>${name}(${username})</div>`;
        }
    })
    .catch(error=>{
        console.error('Error:', error);
    });
}

function updateName() {
    const nameUpdateElement = document.getElementById('nameUpdate');
    const newName = nameUpdateElement.value;
    const data = {
        "name":newName,
    };

    fetch('/api/member/',{
        method:"PATCH",
        headers:{    
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(resp=> {
        if (!resp.ok){
            throw new Error('Network response was not ok');
        }
        return resp.json();
    })
    .then(data=> {
        const divElement = document.getElementById('updateMsg'); 
        if (data.hasOwnProperty("ok") && data.ok) {
            divElement.innerHTML = `<div>更新成功</div>`;
        } else {
            divElement.innerHTML = `<div>更新失敗</div>`;
        }
    })
    .catch(error=>{
        console.error('Error:', error);
    });
}