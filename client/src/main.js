import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		character: character
	}
});

export default app;