import { mergeProps } from 'solid-js';

function CardIcon(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-icon ${merged.class}`.trim()} {...merged}>
      {merged.children}
    </div>
  );
}

function CardTitle(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-title ${merged.class}`.trim()} {...merged}>{merged.children}</div>
  );
}

function CardSubtitle(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-subtitle ${merged.class}`.trim()} {...merged}>{merged.children}</div>
  );
}

function CardHeader(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-header ${merged.class}`.trim()} {...merged}>{merged.children}</div>
  );
}

function CardBody(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-body ${merged.class}`.trim()} {...merged}>{merged.children}</div>
  );
}

function CardFooter(props) {
  const merged = mergeProps({ class: '' }, props);
  return (
    <div class={`cn-card-footer ${merged.class}`.trim()} {...merged}>{merged.children}</div>
  );
}

export function Card(props) {
  const merged = mergeProps({ clickable: false, class: '' }, props);

  const classes = () => {
    const c = ['cn-card'];
    if (merged.clickable) c.push('cn-card-clickable');
    return c.join(' ');
  };

  return (
    <div class={classes()} {...merged}>
      {merged.children}
    </div>
  );
}

Card.Header = CardHeader;
Card.Body = CardBody;
Card.Footer = CardFooter;
Card.Icon = CardIcon;
Card.Title = CardTitle;
Card.Subtitle = CardSubtitle;

export default Card;
