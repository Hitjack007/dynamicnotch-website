const repo = 'https://github.com/Hitjack007/DynamicNotch';

export const app = {
  name: 'DynamicNotch',
  url: 'https://dynamicnotch.marksstuff.com',
  tagline: "Make your MacBook's notch actually useful.",
  repo,
  releases: `${repo}/releases`,
  download: `${repo}/releases/latest`,
  bugReport: `${repo}/issues/new?template=1-bug-report-form.yml`,
  featureRequest: `${repo}/issues/new?template=1-feature-request-form.yml`,
  security: `${repo}/blob/main/SECURITY.md`,
  contributing: `${repo}/blob/main/CONTRIBUTING.md`,
  license: `${repo}/blob/main/LICENSE`,
  brew: 'brew install --cask hitjack007/dynamicnotch/dynamicnotch',
  unquarantine: 'xattr -dr com.apple.quarantine /Applications/DynamicNotch.app',
  requirements: 'macOS 15 Sequoia or later',
  email: 'mark@dynamicnotch.marksstuff.com',
  supportEmail: 'support@dynamicnotch.marksstuff.com',
  legalEmail: 'legal@dynamicnotch.marksstuff.com',
  upstream: { name: 'boring.notch', team: 'TheBoredTeam', url: 'https://github.com/TheBoredTeam/boring.notch' },
  author: { name: 'Mark Greene', url: 'https://marksstuff.com' },
};

export const nav = [
  { href: '/#features', label: 'Features' },
  { href: '/#install', label: 'Install' },
  { href: '/support', label: 'Support' },
  { href: '/privacy', label: 'Privacy' },
];
