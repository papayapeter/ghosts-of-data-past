<script lang="ts">
	export let id: number;

	let hover = false;
	let show = false;
</script>

<span
	class="sidenote__marker"
	class:sidenote--hover={hover}
	on:mouseenter={() => {
		hover = true;
	}}
	on:mouseleave={() => {
		hover = false;
	}}
	on:click={() => {
		show = !show;
	}}>{id}</span
><div
	class="sidenote sidenote--{id % 2 > 0 ? 'left' : 'right'}"
	class:sidenote--hover={hover}
	class:sidenote--show={show}
	on:mouseenter={() => {
		hover = true;
	}}
	on:mouseleave={() => {
		hover = false;
	}}
>
	<span class="sidenote__number">{id}</span><span class="sidenote__text"
		><slot /><span
			class="sidenote__close"
			on:click={() => {
				show = false;
			}}>close</span
		></span
	>
</div>

<style global lang="scss">
	@use '../scss/variables' as *;
	.sidenote__marker {
		font-feature-settings: 'sups' 1;

		padding: 0 0.4em;
		cursor: pointer;

		&.sidenote--hover {
			font-family: $font-family-underline;
		}
	}

	.sidenote {
		float: left;
		clear: left;

		margin: map-get($margin-primary, 'sm') 0;
		padding: 0 map-get($margin-primary, 'sm');
		border-left: solid map-get($border-width, 'sm') map-get($colors, 'foreground');

		font-size: map-get($sidenote-size, 'sm');

		display: none;

		&.sidenote--show {
			display: unset;
		}
	}

	.sidenote__number {
		padding-right: 2em;
	}

	.sidenote__close {
		color: map-get($colors, 'link');

		padding-left: 2em;
		float: right;

		cursor: pointer;

		&:hover {
			color: map-get($colors, 'foreground');
			// text-decoration: underline;
			font-family: $font-family-underline;
			font-weight: 350;
		}
	}

	@media (hover: none) {
		.sidenote__marker {
			color: map-get($colors, 'link');
			font-family: $font-family-underline;
		}

		.sidenote__close {
			// text-decoration: underline;
			font-family: $font-family-underline;
			font-weight: 350;
		}
	}

	@media only screen and (min-width: $breakpoint) {
		.sidenote {
			margin: map-get($margin-primary, 'lg') 0;
			padding: 0 map-get($margin-primary, 'lg');
			border-left: solid map-get($border-width, 'lg') map-get($colors, 'foreground');

			font-size: map-get($sidenote-size, 'lg');
		}
	}

	@media only screen and (min-width: $sidenote-breakpoint) {
		.sidenote {
			width: min(
				$sidenote-width,
				calc((100vw - $container-width) / 2 - 5 * map-get($margin-primary, 'lg'))
			);

			margin: unset;
			margin-bottom: 2 * map-get($margin-primary, 'lg');

			padding: unset;
			padding-top: map-get($margin-primary, 'lg');
			border-top: solid map-get($border-width, 'lg') map-get($colors, 'foreground');
			border-left: unset;

			display: unset;

			&.sidenote--left {
				float: left;
				clear: left;

				margin-left: max(
					calc(($sidenote-width + 3 * map-get($margin-primary, 'lg')) * -1),
					calc((100vw - $container-width) / -2 + 2 * map-get($margin-primary, 'lg'))
				);

				padding-right: map-get($margin-primary, 'lg');
				border-right: solid map-get($border-width, 'lg') map-get($colors, 'background');

				&.sidenote--hover {
					border-right: solid map-get($border-width, 'lg') map-get($colors, 'foreground');
				}
			}
			&.sidenote--right {
				float: right;
				clear: right;

				margin-right: max(
					calc(($sidenote-width + 3 * map-get($margin-primary, 'lg')) * -1),
					calc((100vw - $container-width) / 2 * -1 + 2 * map-get($margin-primary, 'lg'))
				);

				padding-left: map-get($margin-primary, 'lg');
				border-left: solid map-get($border-width, 'lg') map-get($colors, 'background');

				&.sidenote--hover {
					border-left: solid map-get($border-width, 'lg') map-get($colors, 'foreground');
				}
			}
		}

		.sidenote__close {
			display: none;
		}
	}
</style>
