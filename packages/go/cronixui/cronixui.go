package cronixui

import "fmt"

// Version of CronixUI
const Version = "1.0.4"

// ToastType represents toast notification type
type ToastType int

const (
	ToastTypeSuccess ToastType = iota
	ToastTypeError
	ToastTypeWarning
	ToastTypeInfo
)

// Toast represents a toast notification
type Toast struct {
	Title    string
	Message  string
	Type     ToastType
	Duration int
}

// ToastShow displays a toast notification
func ToastShow(message string, opts ...func(*Toast)) *Toast {
	t := &Toast{Message: message, Type: ToastTypeInfo, Duration: 4000}
	for _, opt := range opts {
		opt(t)
	}
	return t
}

// WithTitle sets toast title
func WithTitle(title string) func(*Toast) {
	return func(t *Toast) { t.Title = title }
}

// WithType sets toast type
func WithType(toastType ToastType) func(*Toast) {
	return func(t *Toast) { t.Type = toastType }
}

// WithDuration sets toast duration
func WithDuration(duration int) func(*Toast) {
	return func(t *Toast) { t.Duration = duration }
}

// ToastSuccess shows a success toast
func ToastSuccess(message string) *Toast {
	return ToastShow(message, WithType(ToastTypeSuccess))
}

// ToastError shows an error toast
func ToastError(message string) *Toast {
	return ToastShow(message, WithType(ToastTypeError))
}

// ToastWarning shows a warning toast
func ToastWarning(message string) *Toast {
	return ToastShow(message, WithType(ToastTypeWarning))
}

// ToastInfo shows an info toast
func ToastInfo(message string) *Toast {
	return ToastShow(message, WithType(ToastTypeInfo))
}

// Toggle represents a toggle switch
type Toggle struct {
	on bool
}

// NewToggle creates a new toggle
func NewToggle() *Toggle {
	return &Toggle{}
}

// Toggle flips the toggle state
func (t *Toggle) Toggle() {
	t.on = !t.on
}

// IsOn returns current toggle state
func (t *Toggle) IsOn() bool {
	return t.on
}

// SetOn sets the toggle state
func (t *Toggle) SetOn(value bool) {
	t.on = value
}

// Modal represents a modal dialog
type Modal struct {
	open bool
}

// NewModal creates a new modal
func NewModal() *Modal {
	return &Modal{}
}

// Open opens the modal
func (m *Modal) Open() {
	m.open = true
}

// Close closes the modal
func (m *Modal) Close() {
	m.open = false
}

// IsOpen returns whether modal is open
func (m *Modal) IsOpen() bool {
	return m.open
}

// Dropdown represents a dropdown menu
type Dropdown struct {
	open bool
}

// NewDropdown creates a new dropdown
func NewDropdown() *Dropdown {
	return &Dropdown{}
}

// Open opens the dropdown
func (d *Dropdown) Open() {
	d.open = true
}

// Close closes the dropdown
func (d *Dropdown) Close() {
	d.open = false
}

// Toggle flips dropdown state
func (d *Dropdown) Toggle() {
	d.open = !d.open
}

// IsOpen returns whether dropdown is open
func (d *Dropdown) IsOpen() bool {
	return d.open
}

// Tabs represents a tabs component
type Tabs struct {
	activeIndex int
}

// NewTabs creates new tabs
func NewTabs() *Tabs {
	return &Tabs{activeIndex: 0}
}

// SetActive sets active tab by index
func (t *Tabs) SetActive(index int) {
	t.activeIndex = index
}

// ActiveIndex returns current active index
func (t *Tabs) ActiveIndex() int {
	return t.activeIndex
}

// Accordion represents an accordion component
type Accordion struct {
	openIndices map[int]bool
}

// NewAccordion creates a new accordion
func NewAccordion() *Accordion {
	return &Accordion{openIndices: make(map[int]bool)}
}

// Toggle toggles an accordion item
func (a *Accordion) Toggle(index int) {
	a.openIndices[index] = !a.openIndices[index]
}

// Open opens an accordion item
func (a *Accordion) Open(index int) {
	a.openIndices[index] = true
}

// Close closes an accordion item
func (a *Accordion) Close(index int) {
	a.openIndices[index] = false
}

// OpenAll opens all items up to total
func (a *Accordion) OpenAll(total int) {
	for i := 0; i < total; i++ {
		a.openIndices[i] = true
	}
}

// CloseAll closes all accordion items
func (a *Accordion) CloseAll() {
	a.openIndices = make(map[int]bool)
}

// IsOpen returns whether item is open
func (a *Accordion) IsOpen(index int) bool {
	return a.openIndices[index]
}

// Pagination represents a pagination component
type Pagination struct {
	total   int
	current int
}

// NewPagination creates new pagination
func NewPagination(total, current int) *Pagination {
	if current < 1 {
		current = 1
	}
	if current > total {
		current = total
	}
	return &Pagination{total: total, current: current}
}

// GoTo navigates to a specific page
func (p *Pagination) GoTo(page int) {
	if page >= 1 && page <= p.total {
		p.current = page
	}
}

// Next goes to next page
func (p *Pagination) Next() {
	if p.current < p.total {
		p.current++
	}
}

// Prev goes to previous page
func (p *Pagination) Prev() {
	if p.current > 1 {
		p.current--
	}
}

// Current returns current page
func (p *Pagination) Current() int {
	return p.current
}

// Total returns total pages
func (p *Pagination) Total() int {
	return p.total
}

// CommandPaletteItem represents a command palette item
type CommandPaletteItem struct {
	Title  string
	Kbd    string
	Action func()
}

// CommandPalette represents a command palette
type CommandPalette struct {
	open  bool
	items []CommandPaletteItem
}

// NewCommandPalette creates a new command palette
func NewCommandPalette() *CommandPalette {
	return &CommandPalette{items: make([]CommandPaletteItem, 0)}
}

// Open opens command palette
func (c *CommandPalette) Open() {
	c.open = true
}

// Close closes command palette
func (c *CommandPalette) Close() {
	c.open = false
}

// Toggle toggles command palette
func (c *CommandPalette) Toggle() {
	c.open = !c.open
}

// IsOpen returns whether command palette is open
func (c *CommandPalette) IsOpen() bool {
	return c.open
}

// SetItems sets command items
func (c *CommandPalette) SetItems(items []CommandPaletteItem) {
	c.items = items
}

// Items returns all items
func (c *CommandPalette) Items() []CommandPaletteItem {
	return c.items
}

// Execute executes item by index
func (c *CommandPalette) Execute(index int) {
	if index >= 0 && index < len(c.items) && c.items[index].Action != nil {
		c.items[index].Action()
		c.Close()
	}
}

// SearchItem represents a search result item
type SearchItem struct {
	Title    string
	Subtitle string
	Action   func()
}

// Search represents a search component
type Search struct {
	open  bool
	items []SearchItem
}

// NewSearch creates a new search
func NewSearch() *Search {
	return &Search{items: make([]SearchItem, 0)}
}

// SetItems sets searchable items
func (s *Search) SetItems(items []SearchItem) {
	s.items = items
}

// Filter filters items by query
func (s *Search) Filter(query string) []SearchItem {
	var results []SearchItem
	for _, item := range s.items {
		results = append(results, item)
	}
	return results
}

// Open opens search results
func (s *Search) Open() {
	s.open = true
}

// Close closes search results
func (s *Search) Close() {
	s.open = false
}

// IsOpen returns whether search is open
func (s *Search) IsOpen() bool {
	return s.open
}

// Items returns all items
func (s *Search) Items() []SearchItem {
	return s.items
}

// Select selects and executes item by index
func (s *Search) Select(index int) {
	if index >= 0 && index < len(s.items) && s.items[index].Action != nil {
		s.items[index].Action()
		s.Close()
	}
}

// Init initializes all CronixUI components
func Init() {
	fmt.Println("CronixUI", Version, "initialized")
}
