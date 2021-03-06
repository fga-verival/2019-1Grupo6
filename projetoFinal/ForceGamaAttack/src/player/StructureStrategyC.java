package player;

import java.awt.event.KeyEvent;

import jplay.Keyboard;

public class StructureStrategyC extends Structure {
	
	private Player player;
	double speed = 2.0;
	private final static String sprite = "src/graphics/img/spaceship.png";

	public StructureStrategyC(int x, int y) {
		super(x, y, sprite);
	}
	
	@Override
	public void moveX(double x) {
		if(this.getKeyboard().keyDown(KeyEvent.VK_RIGHT)) {
			this.x += x * speed;
		}
		else if(this.getKeyboard().keyDown(KeyEvent.VK_LEFT)) {
			this.x -= x * speed;
		}
	}
	
	@Override
	public void moveY(double y) {
		if(this.getKeyboard().keyDown(KeyEvent.VK_DOWN)) {
			this.y += y * speed;
		}
		else if(this.getKeyboard().keyDown(KeyEvent.VK_UP)) {
			this.y -= y * speed;
		}
	}
}
