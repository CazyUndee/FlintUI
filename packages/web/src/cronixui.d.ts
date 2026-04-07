declare namespace CronixUI {
  interface ToastOptions {
    title?: string;
    message: string;
    type?: 'success' | 'error' | 'warning' | 'info';
    duration?: number;
  }

  interface PaginationOptions {
    total: number;
    current: number;
    onChange?: (page: number) => void;
  }

  interface SearchItem {
    title: string;
    subtitle?: string;
    action: () => void;
  }

  interface CommandPaletteItem {
    title: string;
    kbd?: string;
    action: () => void;
  }

  interface ModalInstance {
    open(): void;
    close(): void;
  }

  interface DropdownInstance {
    open(): void;
    close(): void;
    toggle(): void;
  }

  interface ToggleInstance {
    toggle(): void;
    isOn(): boolean;
    setOn(value: boolean): void;
  }

  interface TabsInstance {
    setActive(index: number): void;
  }

  interface AccordionInstance {
    toggle(item: HTMLElement): void;
    openAll(): void;
    closeAll(): void;
  }

  interface PaginationInstance {
    goTo(page: number): void;
    render(): void;
  }

  interface CommandPaletteInstance {
    open(): void;
    close(): void;
    setItems(items: CommandPaletteItem[]): void;
  }

  interface SearchInstance {
    setItems(items: SearchItem[]): void;
    filter(query: string): SearchItem[];
    open(): void;
    close(): void;
  }

  interface ToastStatic {
    show(options: ToastOptions): void;
    success(message: string): void;
    error(message: string): void;
    warning(message: string): void;
    info(message: string): void;
  }

  interface NavStatic {
    init(): void;
  }

  interface CronixUIStatic {
    init(): void;
    $(selector: string): HTMLElement | null;
    $$(selector: string): NodeListOf<HTMLElement>;
    createEl(tag: string, className?: string, attrs?: Record<string, string>): HTMLElement;
    Toast: ToastStatic;
    Nav: NavStatic;
    Toggle: new (element: HTMLElement) => ToggleInstance;
    Modal: new (element: HTMLElement) => ModalInstance;
    Dropdown: new (element: HTMLElement) => DropdownInstance;
    Tabs: new (element: HTMLElement) => TabsInstance;
    Accordion: new (element: HTMLElement) => AccordionInstance;
    Pagination: new (element: HTMLElement, options: PaginationOptions) => PaginationInstance;
    CommandPalette: new (element: HTMLElement) => CommandPaletteInstance;
    Search: new (element: HTMLElement) => SearchInstance;
  }
}

declare const CronixUI: CronixUI.CronixUIStatic;
export default CronixUI;
