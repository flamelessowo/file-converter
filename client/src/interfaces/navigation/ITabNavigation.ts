export interface ITabNavigation {
  label: string | Function;
  icon: string;
  to?: string;
  command?: Function;
  url?: string;
  items?: Array<any>;
  disabled?: boolean | Function;
  visible?: boolean | Function;
  target?: string;
  separator?: boolean;
  style?: object;
  class?: string;
  key?: object;
}