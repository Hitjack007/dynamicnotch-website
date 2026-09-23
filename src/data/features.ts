export interface Feature {
	title: string;
	description: string;
}

// Sourced from the app's README feature list, kept in sync with what's shipped.
export const features: Feature[] = [
	{
		title: 'Dynamic notch sizing',
		description: "Expands and contracts based on what's happening on screen.",
	},
	{
		title: 'Responsive spectrogram',
		description: 'Real-time audio visualizer driven by live capture.',
	},
	{
		title: 'Fan & thermal monitoring',
		description: 'Live fan speed and CPU temperature, always in view.',
	},
	{
		title: 'CPU usage',
		description: 'At a glance, always visible.',
	},
	{
		title: 'Caffeine',
		description: 'Prevent sleep directly from the notch.',
	},
	{
		title: 'Custom system HUDs',
		description: 'Replaces macOS volume, brightness, and keyboard backlight overlays.',
	},
	{
		title: 'Music playback',
		description: 'Album art, controls, and now-playing info.',
	},
	{
		title: 'Calendar & Reminders',
		description: 'Upcoming events, right in the notch.',
	},
	{
		title: 'File shelf',
		description: 'Drag files in, AirDrop them out.',
	},
	{
		title: 'Mirror',
		description: 'Quick webcam view whenever you need it.',
	},
	{
		title: 'Battery indicator',
		description: 'Charging status and percentage at a glance.',
	},
	{
		title: 'Gesture controls',
		description: 'Swipe to open and close.',
	},
];
