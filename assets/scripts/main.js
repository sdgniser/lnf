/* Using Showdown: http://showdownjs.com/ */
function to_md(text){
	let target = document.querySelector('.markdown'),
		converter = new showdown.Converter(),
		html = converter.makeHtml(text);

	target.innerHTML = html;
}

/* formats the problem description according to the markdown
 * prob_desc has been defined in the html */
to_md(prob_desc);
