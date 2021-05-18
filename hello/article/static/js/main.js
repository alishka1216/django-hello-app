async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function articleLike (event) {
    event.preventDefault();
    let a = event.currentTarget
    console.log(a)
    let b = a.href
    console.log(b)

    try {
        let result = await makeRequest(b)
        console.log(result)
        currentTarget.innerHTML = '<i class="fas fa-thumbs-up"></i>'
        currentTarget
    }
}

