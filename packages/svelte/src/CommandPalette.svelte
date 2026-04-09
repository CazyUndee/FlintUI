<script>
	import { createEventDispatcher, onMount, tick } from 'svelte';

	export let open = false;
	export let items = [];

	const dispatch = createEventDispatcher();
	let inputEl;
	let selectedIndex = 0;
	let searchTerm = '';

	$: filteredItems = items.filter(item =>
		item.title.toLowerCase().includes(searchTerm.toLowerCase())
	);

	$: resetSelection();

	function resetSelection() {
		selectedIndex = 0;
	}

	async function handleKeydown(event) {
		if (!open) return;

		if (event.key === 'Escape') {
			dispatch('close');
		} else if (event.key === 'ArrowDown') {
			event.preventDefault();
			selectedIndex = Math.min(selectedIndex + 1, filteredItems.length - 1);
		} else if (event.key === 'ArrowUp') {
			event.preventDefault();
			selectedIndex = Math.max(selectedIndex - 1, 0);
		} else if (event.key === 'Enter' && filteredItems[selectedIndex]) {
			dispatch('select', { item: filteredItems[selectedIndex], index: selectedIndex });
		}
	}

	function handleItemClick(item, index) {
		dispatch('select', { item, index });
	}

	function handleBackdropClick(event) {
		if (event.target === event.currentTarget) {
			dispatch('close');
		}
	}

	$: if (open) {
		tick().then(() => {
			inputEl?.focus();
		});
	} else {
		searchTerm = '';
	}

	onMount(() => {
		window.addEventListener('keydown', handleKeydown);
		return () => window.removeEventListener('keydown', handleKeydown);
	});
</script>

<div
	class="cn-command-palette"
	class:cn-command-palette-open={open}
	on:click={handleBackdropClick}
	on:keydown={handleKeydown}
>
	<div class="cn-command-palette-inner">
		<input
			bind:this={inputEl}
			bind:value={searchTerm}
			type="text"
			class="cn-command-palette-input"
			placeholder="Search commands..."
		/>
		<div class="cn-command-palette-results">
			{#each filteredItems as item, index (index)}
				<div
					class="cn-command-item"
					class:cn-command-item-selected={index === selectedIndex}
					on:click={() => handleItemClick(item, index)}
					on:mouseenter={() => (selectedIndex = index)}
					role="button"
					tabindex="0"
				>
					<div>
						<div class="cn-command-item-title">{item.title}</div>
						{#if item.subtitle}
							<div class="cn-command-item-subtitle">{item.subtitle}</div>
						{/if}
					</div>
					{#if item.kbd}
						<div class="cn-command-item-kbd">{item.kbd}</div>
					{/if}
				</div>
			{:else}
				<div class="cn-command-empty">
					No commands found
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.cn-command-palette {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.7);
		z-index: 500;
		display: flex;
		align-items: flex-start;
		justify-content: center;
		padding-top: 15vh;
		opacity: 0;
		visibility: hidden;
		transition: opacity 0.15s ease, visibility 0.15s ease;
	}

	.cn-command-palette-open {
		opacity: 1;
		visibility: visible;
	}

	.cn-command-palette-inner {
		width: 100%;
		max-width: 560px;
		background: #111111;
		border: 1px solid rgba(255, 255, 255, 0.08);
		border-radius: 14px;
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
		transform: scale(0.95);
		transition: transform 0.15s ease;
	}

	.cn-command-palette-open .cn-command-palette-inner {
		transform: scale(1);
	}

	.cn-command-palette-input {
		width: 100%;
		padding: 20px;
		background: transparent;
		border: none;
		border-bottom: 1px solid rgba(255, 255, 255, 0.08);
		font-size: 16px;
		color: #f0ede8;
		outline: none;
		font-family: 'Outfit', sans-serif;
	}

	.cn-command-palette-input::placeholder {
		color: rgba(240, 237, 232, 0.4);
	}

	.cn-command-palette-results {
		max-height: 400px;
		overflow-y: auto;
		padding: 8px;
	}

	.cn-command-palette-results::-webkit-scrollbar {
		width: 8px;
	}

	.cn-command-palette-results::-webkit-scrollbar-track {
		background: transparent;
	}

	.cn-command-palette-results::-webkit-scrollbar-thumb {
		background: rgba(255, 255, 255, 0.1);
		border-radius: 4px;
	}

	.cn-command-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 12px;
		border-radius: 10px;
		cursor: pointer;
		transition: background 0.15s ease;
	}

	.cn-command-item:hover,
	.cn-command-item-selected {
		background: #1a1a1a;
	}

	.cn-command-item-title {
		font-size: 13px;
		color: #f0ede8;
		font-family: 'Outfit', sans-serif;
	}

	.cn-command-item-subtitle {
		font-size: 12px;
		color: rgba(240, 237, 232, 0.5);
		font-family: 'Outfit', sans-serif;
		margin-top: 2px;
	}

	.cn-command-item-kbd {
		margin-left: auto;
		font-size: 11px;
		padding: 4px 8px;
		background: #222222;
		border-radius: 6px;
		color: rgba(240, 237, 232, 0.5);
		font-family: 'Outfit', sans-serif;
	}

	.cn-command-empty {
		padding: 24px;
		text-align: center;
		color: rgba(240, 237, 232, 0.4);
		font-size: 13px;
		font-family: 'Outfit', sans-serif;
	}
</style>
