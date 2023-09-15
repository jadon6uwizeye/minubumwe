export interface ContainerProps {
  border?: boolean;
  children: React.ReactNode;
}

export interface ButtonProps {
  color?: string;
  fixedWidth?: boolean;
  name?: string;
  children: React.ReactNode;
  onClick?: (e?: any) => void;
}

export interface SvgIconProps {
  src: string;
  width: string;
  height: string;
}

export interface InputProps {
  name: string;
  placeholder: string;
  t: any;
  type?: string;
  value?: string;
  onChange: (
    event:
      | React.ChangeEvent<HTMLInputElement>
      | React.ChangeEvent<HTMLTextAreaElement>
  ) => void;
}

export interface validateProps {
  name: string;
  message: string;
  email: string;
}
