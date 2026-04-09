<script>
import { createEventDispatcher } from 'svelte';

export let total = 1;
export let current = 1;
export let onChange = null;

const dispatch = createEventDispatcher();

function goToPage(page) {
	if (page < 1 || page > total || page === current) return;
	if (onChange) onChange(page);
	dispatch('change', { page });
}

function handleKeydown(event, page) {
	if (event.key === 'Enter' || event.key === ' ') {
		event.preventDefault();
		goToPage(page);
	}
}

$: pages = generatePages(total, current);

function generatePages(totalPages, currentPage) {
	if (totalPages <= 7) {
		return Array.from({ length: totalPages }, (_, i) => i + 1);
	}
	
	const pages = [];
	if (currentPage <= 4) {
		pages.push(1, 2, 3, 4, 5, '...', totalPages);
	} else if (currentPage >= totalPages - 3) {
		pages.push(1, '...', totalPages - 4, totalPages - 3, totalPages - 2, totalPages - 1, totalPages);
	} else {
		pages.push(1, '...', currentPage - 1, currentPage, currentPage + 1, '...', totalPages);
	}
	return pages;
}
</script>

<div class="cn-pagination">
	<button
		type="button"
		class="cn-pagination-item"
		disabled={current === 1}
		on:click={() => goToPage(current - 1)}
		on:keydown={(e) => handleKeydown(e, current - 1)}
		aria-label="Previous page"
	>
		<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
			<path d="M15 18l-6-6 6-6"/>
		</svg>
	</button>

	{#each pages as page}
		{#if page === '...'}
			<span class="cn-pagination-item cn-pagination-ellipsis" aria-label="More pages" aria-hidden="true">...</span>
		{:else}
			<button
				type="button"
				class="cn-pagination-item"
				class:cn-pagination-active={page === current}
				disabled={page === current}
				on:click={() => goToPage(page)}
				on:keydown={(e) => handleKeydown(e, page)}
				aria-label="Page {page}"
				aria-current={page === current ? 'page' : undefined}
			>
				{page}
			</button>
		{/if}
	{/each}

	<button
		type="button"
		class="cn-pagination-item"
		disabled={current === total}
		on:click={() => goToPage(current + 1)}
		on:keydown={(e) => handleKeydown(e, current + 1)}
		aria-label="Next page"
	>
		<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
			<path d="M9 18l6-6-6-6"/>
		</svg>
	</button>
</div>

<style>
.cn-pagination {
	display: flex;
	align-items: center;
	gap: 4px;
}

.cn-pagination-item {
	min-width: 32px;
	height: 32px;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 12px;
	font-family: 'Outfit', sans-serif;
	font-weight: 500;
	border-radius: 10px;
	border: 1px solid rgba(255, 255, 255, 0.08);
	background: #111111;
	color: rgba(240, 237, 232, 0.5);
	cursor: pointer;
	transition: all 0.15s ease;
	padding: 0;
}

.cn-pagination-item:hover {
	border-color: rgba(255, 255, 255, 0.15);
	color: #f0ede8;
}

.cn-pagination-item.cn-pagination-active {
	background: #6b2323;
	border-color: #6b2323;
	color: #f0ede8;
}

.cn-pagination-item:disabled {
	opacity: 0.5;
	cursor: not-allowed;
}

.cn-pagination-ellipsis {
	cursor: default;
	border: none;
	background: transparent;
}

.cn-pagination-ellipsis:hover {
	border-color: transparent;
	color: rgba(240, 237, 232, 0.5);
}
</style>
