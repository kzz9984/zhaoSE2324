let greeting = () =>{
    return new Promise((resolve, reject)=>{
        setTimeout(() => {
            resolve('hello world');
        }, 2000);
    });
};

greeting().then((fromResolve)=>{
    console.log(fromResolve);
});