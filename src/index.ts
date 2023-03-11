export default {
	async fetch(request: Request) {
		const url = new URL(request.url);
		const datarange = url.searchParams.get('datarange');



		if (datarange) {
			var selectRange = parseInt(datarange);
		} else {
			var selectRange = 826;
		}

		if (url.pathname === "/random_image") {
			const image_num = Math.floor(Math.random() * selectRange);
			const image_url = `https://rickandmortyapi.com/api/character/avatar/${image_num}.jpeg`;

			const statusCode = 302;
			return Response.redirect(image_url, statusCode);
		} else if (
			url.pathname === "/random_character"
		) {
			const char_num = Math.floor(Math.random() * selectRange);
			const char_url = `https://rickandmortyapi.com/api/character/${char_num}`;

			const statusCode = 302;
			return Response.redirect(char_url, statusCode);
		} else {
			const data = {
				Error: `Missing or invalid path. Visit https://github.com/Thenafi/rickandmortyrandom for usage`,
			};

			const json = JSON.stringify(data, null, 2);

			return new Response(json, {
				status: 400,
				headers: {
					"content-type": "application/json;charset=UTF-8",
				},
				statusText: "Missing or invalid path"
			});
		}
	},
};
