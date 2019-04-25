const title_Input = document.querySelector('input[name=title]');
const slug_Input = document.querySelector('input[name=slug]');

const slugify = (val) => {
	return val.toString().toLowerCase().trim()
	.replace(/&/g, '-and-')
	.replace(/[\s\W-]+/g,'-')
}

title_Input.addEventListener('keyup', (e)=>{
	slug_Input.setAttribute('value', slugify(title_Input.value));
})
