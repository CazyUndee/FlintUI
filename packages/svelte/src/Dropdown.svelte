<script>
	import { createEventDispatcher } from 'svelte';
	import { onMount, onDestroy } from 'svelte';

	export let items = [];
	export let selected = '';

	const dispatch = createEventDispatcher();
	let isOpen = false;
	let dropdownEl;

	function toggle() {
		isOpen = !isOpen;
	}

	function open() {
		isOpen = true;
	}

	function close() {
		isOpen = false;
	}

	function handleSelect(item) {
		const value = typeof item === 'object' ? item.value : item;
		const label = typeof item === 'object' ? item.label : item;
		dispatch('select', { value, label, item });
		selected = label;
		close();
	}

	function handleClickOutside(event) {
		if (dropdownEl && !dropdownEl.contains(event.target)) {
			close();
		}
	}

	function handleKeydown(event) {
		if (event.key === 'Escape') {
			close();
		}
	}

	onMount(() => {
		document.addEventListener('click', handleClickOutside);
		document.addEventListener('keydown', handleKeydown);
	});

	onDestroy(() => {
		document.removeEventListener('click', handleClickOutside);
		document.removeEventListener('keydown', handleKeydown);
	});
</script>

<div
	class="cn-dropdown"
	class:cn-dropdown-open={isOpen}
	bind:this={dropdownEl}
>
	<slot {isOpen} {open} {close} {toggle}>
		<button
			type="button"
			class="cn-dropdown-trigger"
			on:click={toggle}
			aria-haspopup="true"
			aria-expanded={isOpen}
		>
			{selected || 'Select...'}
		</button>
	</slot>

	<div class="cn-dropdown-menu" role="menu">
		{#each items as item, i}
			{#if item && item.divider}
				<div class="cn-dropdown-divider" role="separator"></div>
			{:else}
				<div
					class="cn-dropdown-item"
					class:cn-dropdown-item-active={typeof item === 'object'
						? item.label === selected
						: item === selected}
					on:click={() => handleSelect(item)}
					on:keydown={() => {}}
					role="menuitem"
					tabindex="0"
				>
					{#if typeof item === 'object'}
						{#if item.icon}
							<span class="cn-dropdown-item-icon">{item.icon}</span>
						{/if}
						<span class="cn-dropdown-item-label">{item.label}</span>
					{:else}
						{item}
					{/if}
				</div>
			{/if}
		{/each}
	</div>
</div>

<style>
	.cn-dropdown {
		position: relative;
		display: inline-block;
	}

	.cn-dropdown-menu {
		position: absolute;
		top: 100%;
		left: 0;
		min-width: 180px;
		background: #111111;
		border: 1px solid rgba(255, 255, 255, 0.08);
		border-radius: 10px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
		z-index: 100;
		opacity: 0;
		visibility: hidden;
		transform: translateY(-8px);
		transition: all 0.15s ease;
	}

	.cn-dropdown.cn-dropdown-open .cn-dropdown-menu {
		opacity: 1;
		visibility: visible;
		transform: translateY(4px);
	}

	.cn-dropdown-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 8px 16px;
		font-size: 13px;
		color: #f0ede8;
		cursor: pointer;
		transition: background 0.15s ease;
	}

	.cn-dropdown-item:hover {
		background: #1a1a1a;
	}

	.cn-dropdown-item:first-child {
		border-radius: 10px 10px 0 0;
	}

	.cn-dropdown-item:last-child {
		border-radius: 0 0 10px 10px;
	}

	.cn-dropdown-item-active {
		background: rgba(255, 255, 255, 0.05);
	}

	.cn-dropdown-divider {
		height: 1px;
		background: rgba(255, 255, 255, 0.08);
		margin: 8px 0;
	}

	.cn-dropdown-trigger {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 8px 16px;
		font-size: 13px;
		color: #f0ede8;
		background: #111111;
		border: 1px solid rgba(255, 255, 255, 0.08);
		border-radius: 10px;
		cursor: pointer;
		transition: background 0.15s ease, border-color 0.15s ease;
	}

	.cn-dropdown-trigger:hover {
		background: #1a1a1a;
		border-color: rgba(255, 255, 255, 0.12);
	}
</style>
