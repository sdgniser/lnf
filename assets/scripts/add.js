function main(e) {
	let selectCategory = document.querySelector('#id_category');
	selectCategory.onchange = function(e) {
		if (selectCategory.value === "Other") {
			selectCategory.setAttribute("name", "");

			let inputCategory = document.createElement("input");
			inputCategory.id = "id_category_other";
			inputCategory.setAttribute("type", "text");
			inputCategory.setAttribute("name", "category");
			inputCategory.setAttribute("required", "");

			selectCategory.parentNode.appendChild(inputCategory);
		} else {
			let inputCategory = document.querySelector("#id_category_other");
			if (inputCategory) {
				inputCategory.parentNode.removeChild(inputCategory);
				selectCategory.setAttribute("name", "category");
			}
		}
	};
}

window.onload = main;
