<script>
import { createEventDispatcher, onMount, onDestroy } from 'svelte';

export let message = '';
export let type = 'info';
export let duration = 3000;

const dispatch = createEventDispatcher();

let visible = true;
let isLeaving = false;
let timeoutId;

const icons = {
	info: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.5"/><path d="M10 14V9M10 6.5V6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>`,
	success: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.5"/><path d="M6.5 10.5L9 13L13.5 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
	warning: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10 2L2 18H18L10 2Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 14V11M10 8.5V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>`,
	error: `<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.5"/><path d="M7.5 7.5L12.5 12.5M12.5 7.5L7.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>`
};

const iconColors = {
	info: '#6ba8c4',
	success: '#6bc47a',
	warning: '#c4a43a',
	error: '#c46b6b'
};

function close() {
	isLeaving = true;
	setTimeout(() => {
		visible = false;
		dispatch('close');
	}, 200);
}

onMount(() => {
	if (duration > 0) {
		timeoutId = setTimeout(close, duration);
	}
});

onDestroy(() => {
	if (timeoutId) {
		clearTimeout(timeoutId);
	}
});
</script>

{#if visible}
<div class="cn-toast" class:cn-toast-leaving={isLeaving} role="alert">
	<div class="cn-toast-icon" style="color: {iconColors[type]}">
		{@html icons[type]}
	</div>
	<div class="cn-toast-message">{message}</div>
	<button class="cn-toast-close" on:click={close} aria-label="Close">
		<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
			<path d="M5 5L15 15M15 5L5 15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
		</svg>
	</button>
</div>
{/if}

<style>
.cn-toast {
	min-width: 300px;
	max-width: 450px;
	padding: 16px;
	background: #111111;
	border: 1px solid rgba(255, 255, 255, 0.08);
	border-radius: 10px;
	box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
	display: flex;
	align-items: flex-start;
	gap: 12px;
	animation: cn-toast-in 0.3s ease;
	font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.cn-toast-leaving {
	animation: cn-toast-out 0.2s ease forwards;
}

@keyframes cn-toast-in {
	from {
		opacity: 0;
		transform: translateX(100%);
	}
	to {
		opacity: 1;
		transform: translateX(0);
	}
}

@keyframes cn-toast-out {
	from {
		opacity: 1;
		transform: translateX(0);
	}
	to {
		opacity: 0;
		transform: translateX(100%);
	}
}

.cn-toast-icon {
	flex-shrink: 0;
	width: 20px;
	height: 20px;
}

.cn-toast-icon :global(svg) {
	width: 100%;
	height: 100%;
}

.cn-toast-message {
	flex: 1;
	font-size: 13px;
	color: #f0ede8;
	line-height: 1.5;
}

.cn-toast-close {
	flex-shrink: 0;
	width: 20px;
	height: 20px;
	padding: 0;
	border: none;
	background: transparent;
	color: rgba(240, 237, 232, 0.5);
	cursor: pointer;
	transition: color 0.15s ease;
}

.cn-toast-close:hover {
	color: #f0ede8;
}

.cn-toast-close svg {
	width: 100%;
	height: 100%;
}
</style>
