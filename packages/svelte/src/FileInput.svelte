<script>
	import { createEventDispatcher } from 'svelte';

	export let accept = '';
	export let multiple = false;
	export let disabled = false;

	const dispatch = createEventDispatcher();

	let isDragging = false;
	let fileName = '';

	function handleChange(event) {
		const files = event.target.files;
		if (files.length > 0) {
			fileName = Array.from(files).map(f => f.name).join(', ');
		}
		dispatch('change', {
			files: files,
			fileList: Array.from(files)
		});
	}

	function handleDragOver(event) {
		event.preventDefault();
		event.stopPropagation();
		if (!disabled) {
			isDragging = true;
		}
	}

	function handleDragLeave(event) {
		event.preventDefault();
		event.stopPropagation();
		isDragging = false;
	}

	function handleDrop(event) {
		event.preventDefault();
		event.stopPropagation();
		isDragging = false;
		const files = event.dataTransfer.files;
		if (files.length > 0) {
			fileName = Array.from(files).map(f => f.name).join(', ');
			dispatch('change', {
				files,
				fileList: Array.from(files)
			});
		}
	}
</script>

<div class="cn-file-input" class:cn-file-input-disabled={disabled} class:cn-file-input-dragging={isDragging} class:cn-file-input-has-file={fileName}>
	<input
		type="file"
		{accept}
		{multiple}
		{disabled}
		on:change={handleChange}
	/>
	<label
		class="cn-file-input-label"
		on:dragover={handleDragOver}
		on:dragleave={handleDragLeave}
		on:drop={handleDrop}
	>
		<svg class="cn-file-input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
			<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
			<polyline points="17 8 12 3 7 8" />
			<line x1="12" y1="3" x2="12" y2="15" />
		</svg>
		<span class="cn-file-input-text">
			{#if fileName}
				<span>{fileName}</span>
			{:else}
				<span>Click to upload</span> or drag and drop
			{/if}
		</span>
	</label>
</div>

<style>
	.cn-file-input {
		position: relative;
	}

	.cn-file-input input[type="file"] {
		position: absolute;
		opacity: 0;
		width: 100%;
		height: 100%;
		cursor: pointer;
	}

	.cn-file-input-label {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 12px;
		padding: 32px;
		background: #111111;
		border: 2px dashed rgba(255, 255, 255, 0.08);
		border-radius: 10px;
		transition: border-color 0.15s ease, background 0.15s ease;
	}

	.cn-file-input:hover .cn-file-input-label {
		border-color: rgba(255, 255, 255, 0.15);
	}

	.cn-file-input-dragging .cn-file-input-label {
		border-color: #6b2323;
		background: rgba(107, 35, 35, 0.1);
	}

	.cn-file-input-icon {
		width: 40px;
		height: 40px;
		color: rgba(240, 237, 232, 0.5);
	}

	.cn-file-input-text {
		font-size: 13px;
		color: rgba(240, 237, 232, 0.5);
	}

	.cn-file-input-text span {
		color: #c97a7a;
		text-decoration: underline;
	}

	.cn-file-input-disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.cn-file-input-disabled input[type="file"] {
		cursor: not-allowed;
	}

	.cn-file-input-has-file .cn-file-input-label {
		border-color: rgba(107, 35, 35, 0.3);
	}
</style>
