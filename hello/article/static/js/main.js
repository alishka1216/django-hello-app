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

    let a = event.currentTarget //достаём aшку из лайка
    console.log(a)
    let b = a.href //достаем ссылку
    console.log(b)
    try{
        let result = await makeRequest(b)
        console.log(a.innerHTML)
        a.innerHTML = '<i class="fas fa-thumbs-up"></i>'
        a.setAttribute('href', b.replace('Articlelike', 'Articleunlike'))
        a.onclick = unlikeArticle
        let id = a.dataset.articlecounter
        let counter = document.getElementById(id)
        counter.innerText = result
    }
    catch (error){
        console.log(error)
    }
}

async function unlikeArticle(event){
    event.preventDefault();
    let a = event.currentTarget
    let b = a.href
    try {
        let result = await makeRequest(b)
        a.innerHTML = '<i class="far fa-thumbs-up"></i>'
        a.setAttribute('href', b.replace('Articleunlike', 'Articlelike'))
        a.onclick = articleLike
        let id = a.dataset.articlecounter
        let counter = document.getElementById(id)
        counter.innerText = result
    }
        catch (error){
        console.log(error)
    }
}
