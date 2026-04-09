import componentsJson from '@spec/components.json';
import tokensJson from '@spec/tokens.json';

export type SpecProp = {
  name: string;
  type: string;
  values?: string[];
  items?: Record<string, string>;
  default?: string | boolean | number;
  required?: boolean;
};

export type SpecComponent = {
  name: string;
  prefix: string;
  category: string;
  props: SpecProp[];
  slots?: string[];
  events?: string[];
};

export const components = componentsJson.components as SpecComponent[];
export const tokens = tokensJson;

export function getComponent(name: string) {
  return components.find((component) => component.name.toLowerCase() === name.toLowerCase());
}
