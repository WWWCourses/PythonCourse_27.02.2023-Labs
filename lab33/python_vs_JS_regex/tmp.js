let text = `jkdsjkds 123
ABC
456`;

let rx = /123.abc/is;

if(text.match(rx)){
	console.log(`match`);
}else{
	console.log(`no match`);
}


