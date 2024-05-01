package utils

trait Display {
  implicit class ShowAny[T](x: T) {
    def show(): Unit = println(x)
  }
}
